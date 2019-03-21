%--------------------------------------------------------------------------
clear all      % Clear workspace
%--------------------------------------------------------------------------

%--------------------------------------------------------------------------
% Set parameter values
%--------------------------------------------------------------------------
beta    = 0.99;     % Discount factor
b       = 0.75;     % Unemployment income
alpha= 1/3;      % Wage offer probability
lambda     = 0.02;     % Job loss probability
w_min   = 0;        % Minimum wage offer 
w_max   = 2;        % Maximum wage offer 
s_cost = 0.2;   % exogeneous cost for job searching
nsu_max =  0.5;   % Maximum utlity for home production
nsu_min = nsu_max -1;  % Minium utlity for home production
%--------------------------------------------------------------------------
%--------------------------------------------------------------------------
n           = 1e+4;         % Number of grid points for wage grid
%--------------------------------------------------------------------------
wage        = linspace(w_min,w_max,n)';         % Wage grid
wage_cdf    = (wage - w_min)/(w_max-w_min);     % CDF (uniform) of wages
nsu = linspace(nsu_min,nsu_max,n)';             % not search utility gird
nsu_cdf    = (nsu - nsu_min)/(nsu_max-nsu_min);  % CDF for NSU
%--------------------------------------------------------------------------
S = -s_cost;   % Initial guess for value functon: searching  
NS = nsu;           % Initial guess for value functon: not searching  
U    = b;           % Initial guess of value function: unemployment
W    = wage;        % Initial guess of value function: employment

%--------------------------------------------------------------------------
crit    = 1e-12;    % Convergence criterion
metric  = 1;        % Convergence metric
%--------------------------------------------------------------------------

%--------------------------------------------------------------------------
while metric > crit     % Start iteration
%--------------------------------------------------------------------------
    res_wage = wage( find(W-U>0,1,'first') );
    res_nsu = nsu( find(S-NS>0,1,'first') );
    inactRate = (res_nsu - nsu_min)/(nsu_max-nsu_min);
    P = @(x) (1 - inactRate - lambda/(lambda + alpha* (res_wage - x -2)/2)) ...
    - (1 - inactRate - lambda/(lambda + alpha* (res_wage - x -2)/2))*(x+ res-wage)/2;
    disp(fmincon(P, w_max));
    break
%--------------------------------------------------------------------------
% New value function: employment
%--------------------------------------------------------------------------
    W_new = wage + beta*(1-lambda)*W + lambda*beta*U - s_cost;
%--------------------------------------------------------------------------
%--------------------------------------------------------------------------
% New value function: unemployment
%--------------------------------------------------------------------------
    U_new = b + beta* max(NS, S) - s_cost;
    S_new = alpha*(1 - res_cdf)*avg_wage + (alpha*res_cdf + 1 - alpha)*U - s_cost;
    NS_new = nsu + beta* max(NS, S);
%--------------------------------------------------------------------------
% Compute maximum distance (metric) between old and new value functions
%--------------------------------------------------------------------------
    metric = max([ abs(W_new-W)./( 1+abs(W) ); abs(U_new-U)./( 1+abs(U) ...
        ); abs(NS_new-NS)./( 1+abs(NS) ); abs(S_new-S)./( 1+abs(S) ) ] );
%--------------------------------------------------------------------------
    U = U_new;      % Update guess of value function: unemployment
    W = W_new;      % Update guess of value function: employment
    S = S_new;      % Update guess of VF search
    NS = NS_new;    % Update guess of VF not search
    P = P_new;
%--------------------------------------------------------------------------
end
%--------------------------------------------------------------------------
res_wage = wage( find(W-U>0,1,'first') );   % Find reservation wage
res_nsu = nsu( find(S-NS>0,1,'first') );   % Find reservation wage
%--------------------------------------------------------------------------

%--------------------------------------------------------------------------

%--------------------------------------------------------------------------
% Plot value functions
%--------------------------------------------------------------------------
U = res_wage/(1-beta);
W = @(w) ( w + lambda*beta*U )/( 1 - beta*(1-lambda) );
%--------------------------------------------------------------------------
wage = w_min:0.01:w_max;
%--------------------------------------------------------------------------
%--------------------------------------------------------------------------
% plot(wage, W(wage),'b', wage,wage./wage*U,'r')
%--------------------------------------------------------------------------
uRrate      = lambda/( lambda + alpha*(1-res_wage/(w_max-w_min)) );  % Unemployment rate
uDuration   = 1/( alpha*(1-res_wage/(w_max-w_min)) );          % Duration of unemployment
eDuration   = 1/lambda;                                            % Duration of employment
inactRate = 1;  % Percentage of people not searching job with such wage level
%--------------------------------------------------------------------------
avg_wage    = (w_max + res_wage)/2;    % Average wage
%--------------------------------------------------------------------------

%--------------------------------------------------------------------------
% Display output
%--------------------------------------------------------------------------
disp('rWage       u-rate     u-duration  e-duration   avg_wage res_nsu')
disp( num2str( [res_wage    uRrate  uDuration   eDuration   avg_wage res_nsu], '%12.3f') )
%--------------------------------------------------------------------------



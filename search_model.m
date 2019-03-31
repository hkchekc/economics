clear all

%--------------------------------------------------------------------------
% Set parameter values
%--------------------------------------------------------------------------
beta   = 0.8;   % Discount Factor
b      = 0.6;   % Unemployment income (not flow utility) (around 60%  of net income for Germany)
alpha  = 0.67;  % Wage offer probability
lambda = 0.011; % Job loss probability 
w_min  = 0;     % Minimum wage offer
w_max  = 2;     % Max wage offer
n_min  = -1.75; % Minimum utility for home production when not spending time on job searching
n_max  = 1.75;  % Maximum utility for home production when not spending time on job searching
s_cost = 0.4;   % Cost of searching job

%--------------------------------------------------------------------------
% Run VFI to compute the reservation wage
%--------------------------------------------------------------------------

n        = 1e+3;                        % Number of grids for wage offers and also the home production utility
crit     = 1e-12;                       % Convergence criterion
metric   = 1;                           % Convergence metric
wage     = linspace(w_min,w_max,n);     % Wage grid
wage_pdf = 1/n;                         % Probability mass of discreate uniform grids
ns_range = linspace(n_min, n_max, n)';  % Not-searching grid
disp(num2str([n, crit]));
%--------------------------------------------------------------------------
% Initial Guess
%--------------------------------------------------------------------------
U  = ones(n, 1)*b;                              % Initial guess of value function: unemployment  (n,1 vector)
W  = ones(n, 1)*wage;                           % Initial guess of value function: employment (n,n matrix)
S  = ones(n, 1)*b;                              % Initial guess of value function: searching  (n,1 vector)
NS = ns_range;                                  % Initial guess of value function: not searching  (n,1 vector)
res_wage = U;                                   % Initial guess of reservation wage for all ns-utility  (n,1 vector)
res_cdf = (res_wage - w_min)./(w_max - w_min);  % (n,1 vector)

while metric > crit     % Start iteration

    %--------------------------------------------------------------------------
    % Update value functions
    %--------------------------------------------------------------------------
    wage_mask = (wage'  >  res_wage);  % logical mask for offers that will not be accepted
    exp_W = [];
    for i = 1:n
        s = sum(W(i, wage_mask));
        if isempty(s)
           s = 0;
        end
        exp_W = [exp_W; s];
    end
    % exp_W = sum(W(:, wage_mask)')' is an alternative to the loop and append above
    exp_W(isnan(exp_W)) = 0;
    %--------------------------------------------------------------------------
    % Update Value Functions (details in the description file)
    %--------------------------------------------------------------------------
    S_new  = alpha.*(1-res_cdf).*exp_W.*wage_pdf./(1-res_cdf)+(alpha.*res_cdf+1-alpha).* U -s_cost;
    NS_new = ns_range+max(S, NS).*beta;
    W_new  = ones(n, 1)*wage + beta.*((1-lambda).*W+lambda.*U*ones(1, n));
    U_new  = b+beta.*max(S, NS);
    %--------------------------------------------------------------------------
    % Update reservation wage for all agents
    %--------------------------------------------------------------------------
    for idx = 1:length(W)
        rw = wage(find(W(idx, :)-U(idx)>0, 1 ,'first') ); % Find the res_wage
        if rw
            res_wage(idx) = rw;
        else
            res_wage(idx) = w_max;                         % This agent will never work
        end
    end
    res_cdf = (res_wage-w_min)./(w_max-w_min);             % recalculate the CDF
%--------------------------------------------------------------------------
% Update metric
%--------------------------------------------------------------------------
    metric = max([ reshape(abs(W_new-W)./( 1+abs(W) ), [n*n, 1]); ...
        abs(U_new-U)./( 1+abs(U) ); abs(S_new-S)./( 1+abs(S) ); abs(NS_new-NS)./( 1+abs(NS) )] );
    S_new(isnan(S_new))   = 0;      % Ensure the VFs keep in shape
    NS_new(isnan(NS_new)) = 0;
    U_new(isnan(U_new))   = 0;
    W_new(isnan(W_new))   = 0;
    rho = 1;                        % Lowering rho can potentially fix convergence problem
    U  = rho.*U_new+(1-rho).*U;     % Update guess of value function: unemployment
    W  = rho.*W_new+(1-rho).*W;     % Update guess of value function: employment
    S  = rho.*S_new+(1-rho).*S;     % Update guess of value function: searching
    NS = rho.*NS_new+(1-rho).*NS;   % Update guess of value function: not searching
end
%--------------------------------------------------------------------------
% end of VFI
%---------------------------------------------------------------------------
U  = U_new;  % Last update without rho
W  = W_new;
S  = S_new;
NS = NS_new;
%--------------------------------------------------------------------------
% Find reseveration utility for no job searching
% Inactivity Rate related is our Target
%--------------------------------------------------------------------------
res_ns    = ns_range( find(NS-S > 0, 1, 'first'));  % How much to produce in home production can induce people not to work
inactRate = (n_max - res_ns)/(n_max - n_min);
 % Make sure the script doesn't break when reseveration utility is higher than max home production n_max
if isempty(res_ns)
   res_ns    = n_max;
   inactRate = 0;
end
%--------------------------------------------------------------------------
% Find also some non-target observables to check validity
%--------------------------------------------------------------------------
res_mask     = (S > NS);
avg_res_wage = sum(res_wage(res_mask))/length(res_wage(res_mask));  % Reservation Wage
uRate        = (lambda-lambda*inactRate)/(lambda+alpha*(1-inactRate)*(1-avg_res_wage/(w_max-w_min))); % Unemployment Rate
eDuration    = 1/lambda;                                            % Duration of employment
avg_wage     = (w_max+avg_res_wage)/(w_max-w_min);                  % Average wage
hpWorkRatio  = (n_max +res_ns)/2/avg_wage;                          % Ratio of average home production value to average wage
sCostWorkRat = s_cost/avg_wage;                                     % Ratio of searching cost to wage
%--------------------------------------------------------------------------
% Display output
%--------------------------------------------------------------------------
disp('rHomeProd   rWage       u-rate     e-duration  avg_wage   inactRate   hProd/Work   sCost/Work')
disp( num2str( [res_ns avg_res_wage    uRate    eDuration   avg_wage inactRate hpWorkRatio sCostWorkRat], '%12.3f') )
%--------------------------------------------------------------------------
%--------------------------------------------------------------------------
% Stimulation
% Based on the res_ns and res_wage above
%--------------------------------------------------------------------------
% Idea of the stochastic utility for not searching
% A person can change her utility for home production (not
% search). For example, one can suddenly came up with an brilliant
% idea to be done at home or can feel very guilty to not search for job
% because even her youngest sister start working.
%--------------------------------------------------------------------------
% First, define number of agents and periods
%--------------------------------------------------------------------------

T = 300;            % Number of periods
no = 1000;          % Number of agents

%--------------------------------------------------------------------------
employed_vec     = zeros(no, 1);  % Stores which agent get employed / Start with all unemployed
no_search_vec    = zeros(no, 1);  % Stores which agent search and which agent not
wage_record      = zeros(no, 1);  % Store the wage accepted by agent
em_history       = [];            % Store employment data for every period for plotting
search_history   = [];            % Store job search record for plotting
avg_wage_history = [];            % Store the average wage each period for plotting
%--------------------------------------------------------------------------
% Assign randomly initial no-job-search utility to agents
%--------------------------------------------------------------------------
ori_ns_vec = (n_max-n_min).*rand(no, 1)+n_min;
ns_vec     = ori_ns_vec;
%--------------------------------------------------------------------------
% Starts iteration from period 1 to period T
%--------------------------------------------------------------------------
for t = 1:T
    ran_lambda = find(rand(no, 1) < lambda);  % Randomly choose someone lossing job based on lambda
    for i = 1: length(ran_lambda)             % Clear the employed status and wage record for agents who lost their job
        pos = ran_lambda(i);
        employed_vec(pos) = 0;
        wage_record(pos) = 0;
    end
    ns_adjust      = (rand(no, 1)-0.500).*2.*0.1;            % Generate random adjustment for no-search utility
    ns_vec         = 0.0*ori_ns_vec+1.*ns_vec+ns_adjust; % Stochastically Update the no searching utility for all agents
    no_search_mask = (ns_vec > res_ns);                      % Logical mask for no-job-searching agents
    for i = 1: length(no_search_mask)                        % Loop to record the ones who do not search for job
        if no_search_mask(i) == 1 && employed_vec(i) == 0    % Employed agent should not be updated to not searching
            no_search_vec(i) = 1;                            % Mark agents who do not search for job as 1
        else
            no_search_vec(i) = 0;
        end
    end
    offer_vec         = (w_max-w_min).*rand(no, 1)+w_min; % Generate wage offers
    accept_offer_mask = (offer_vec > avg_res_wage);       % Observe which agents will accept offer
    ran_alpha = find(rand(no, 1) < alpha);                % Decide which agents will be getting job offer
    for i = 1: length(ran_alpha)                          % Loop to update to employed agents and store wage accepted
        pos = ran_alpha(i);                               % Updates only applied to agents who search for job and not employed yet
        if accept_offer_mask(pos) == 1 && employed_vec(pos) == 0 && no_search_vec(pos) == 0
            employed_vec(pos) = 1;
            wage_record(pos) = offer_vec(pos);
        end
    end
    %--------------------------------------------------------------------------
    % Store records for current period T
    %--------------------------------------------------------------------------
    avg_wage         = sum(wage_record)/sum(employed_vec);   % The average wage should not include unemployed and inactive agents
    avg_wage_history = [avg_wage_history; avg_wage];
    em_history       = [em_history; sum(employed_vec)/no];
    search_history   = [search_history; 1-sum(no_search_vec)/no];  % Number of agents who are NOT inactive
end
%--------------------------------------------------------------------------
% End of Stimulation
%--------------------------------------------------------------------------
% Plot the graphs
%--------------------------------------------------------------------------
plot([1:T], em_history, 'b', [1:T], search_history, 'r');
figure();
plot([1:T], avg_wage_history, 'r');

%--------------------------------------------------------------------------


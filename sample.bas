% LET variable = expression	'LET Function'
% IF condition THEN statement	'IF, THEN statement'
% ELSE IF statement2		'ELSE IF Statement'
% ELSE statement3		'ELSE Statement'
% FOR				'FOR Statement'
	% statements													
	% NEXT
% FOR I= start-number TO stop-number [ STEP = stepsize] 'Here, we have set our index variable I and its parameters.'
							'STEP is our unit of difference between successive terms'
							'STEP increment is 1 by default'
% DIM Score(5) 			'DIM creates enumerated instances of, in this case, Score. Stands for Dimension'
% () ^ * / + -			'Nummeric Operators'
% < <= <> = => >		'Relational Operators'
% AND OR NOT			'Logical Operators'

% 'BASIC Special Variables'
	% CASE 			'Observation Number'
	% BOF			'Logical Variable for Beginning of File (BOF)'
	% EOF			'Logical Variable for End of File (EOF)'

% 'Function form for mathematical expresiions'
	% FUNCTION(variable1, variable2, ...)

% 'Multiple argument functions'
	% AVG()			'Arithmetic Mean'
	% MAX()			'Maximum'
	% MIN()			'Minimum'
	% MIS()			'Number of missing variables'
	% STD()			'Standard Deviation'
	% SUM()			'Summation'

% 'Single argument functions'
	% ABS()			'Absolute Value'
	% ACS()			'Arc Cosine'
	% ASN()			'Arc Sine'
	% ATH()			'Arc Hyperbolic Tangent'
	% ATN()			'Arc Tangent'
	% COS()			'Cosine'
	% EXP()			'Exponential'
	% LOG()			'Natural Logarithm'
	% SIN()			'Sine'
	% SQR()			'Square Root'
	% TAN()			'Tangent'

% 'Distribution Type Letters'
% 'First letter identifies the distribution.
	% RN	'Random Number'
	% CF	'Cumulative'
	% DF	'Density'
	% IF	'Inverse'
% 'Probability Distributions'
% 'First letter identifies the distribution. Remain letters define function: RN (Random Number), CF 'Cumulative''
% 'DF (Density), IF (Inverse)'
	% B	'Beta'
	% N	'Binomial'
	% X	'Chi-square'
	% E	'Exponential'
	% F	'F'
	% G	'Gamma'
	% L	'Logistic'
	% Z	'Normal (Standard)'
	% P	'Poisson'
	% S	'Studentized'
	% T	't'
	% U	'Uniform'
	% W	'Weibull'

% 'The following code generates 10 random draws from a chi-square variable with 35 degrees of freedom'
% DIM CHISQ(10)
	% FOR I= 1 TO 10
	% LET CHISQ(I)=XRN(35)
	% NEXT

% 'Missing values are output as a single dot '.''


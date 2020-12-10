fid = fopen('day10.txt');
S = textscan(fid, '%d');
fclose(fid);

s = size(S{1});

A=S{1};

B=sort(A); 
B(94,1) = B(93,1)+3;
jolt1 = 0;
jolt3 = 0;
C(1) = 1;
gr = 1;
for i =2:1:s(1,1)+1
   C(i)=B(i)-B(i-1);
   if C(i)==1
       jolt1 = jolt1+1;
       gr = gr+1;
   elseif C(i)==3
       jolt3 = jolt3+1;
       G(i-1) = gr;
       gr = 0;
   end
   if C(i)>3
       'error'
   end
end


jolt1 = jolt1 +1;
jolt3 = jolt3;
answe1 = jolt1*jolt3;

% part 2

no1 = sum(G==1);
no2 = sum(G==2);
no3 = sum(G==3);
no4 = sum(G==4);
comb = 7^(no4)*4^(no3)*2^(no2)

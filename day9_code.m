fid = fopen('day9.txt','r');
inp = textscan(fid,'%d');
fclose(fid);

A = inp{1}; s = size(A);

for i=26:1:1000
    is=0;
    for j=i-25:1:i-1
        for k=j+1:1:j+24
            if A(i)==A(j)+A(k)
               is=is+1; 
            end
        end
    end
    if is==0
        A(i);
        break
    end
end

% part 2
no_position=i; %505
disp('part 1')
no = A(i) %14144619

p1 = 0;
for i=1:1:1000
    sum(i) = 0;
    cond = 0;
    for j=i:1:1000
        if cond ==0
            if sum(i) + A(j)<= no
                sum(i) = sum(i) + A(j);
                number(i,j) = A(j);
            elseif sum(i) + A(j) > no
                cond = cond+1;
            end
        elseif sum(i) == no
            p1 = i 
            p2 = j
            number(i,j) = A(j);
        end
        if p1~=0
            break
        end
    end
end

c = sort(number(p1,:)); 
disp('part 2')
res = min(c(c~=0)) + max(c)
 
  
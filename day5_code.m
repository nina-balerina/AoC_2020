fid = fopen('day5.txt');
S = textscan(fid, '%s');
fclose(fid);

A = S{1};
for i=1:1:799
    B = A{i};
    s = size(B);
    C(i,1:s(1,2))=B;
end

for i=1:1:799
    i;
        L1 = 0;
        L2 = 127;
    for j=1:1:7
        j;
        mid = (L2+L1)/2;
        if C(i,j)=='B' %upper half
            L1 = ceil(mid);
        elseif C(i,j)=='F' %lower half
            L2 = floor(mid);
        end
        [L1,L2];
    end
    row(i) = L1;
    
        L3 = 0;
        L4 = 7;
    for k=8:1:10
        mid2 = (L4+L3)/2;
        if C(i,k)=='R' %upper half
            L3 = ceil(mid2);
        elseif C(i,k)=='L' %lower half
            L4 = floor(mid2);
        end
    end
    col(i) = L3;
    res(i) = 8*row(i) + col(i);
end

disp('part 1')
max(res)

D = sort(res);
for i =2:1:799
    dif(i) = D(i) - D(i-1);
    if dif(i)>1
        seats = [D(i-1), D(i)];
    end
end

disp('part 2')
seats(1,2)-1



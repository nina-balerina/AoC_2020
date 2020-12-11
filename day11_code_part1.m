tic
fid = fopen('day11.txt');
S = textscan(fid,'%s');
fclose(fid);

A = S{1};
s1 = size(A);

for i=1:1:s1(1,1)
    B(i,:) = A{i};
end
s2 = size(B);

% first change - all seats become occupied
for i=1:1:s2(1,1)
    for j=1:1:s2(1,2)
        if B(i,j)=='L'
            B(i,j)='#';
        end
    end
end
toc

% further changes with the two given conditions

no = 1;
cond = 0;

while (cond==0)
 
    C = B;
    no = no+1;
    for i=1:1:s2(1,1)
        for j=1:1:s2(1,2)
            if (i==1)&&(j==1)
                oc1 = [0,0,0];
                oc2 = [0,0,(C(i,j+1)=='#')];
                oc3 = [0,(C(i+1,j:j+1)=='#')];
            elseif (i==1)&&(j==s2(1,2))
                oc1 = [0,0,0];
                oc2 = [(C(i,j-1)=='#'),0,0];
                oc3 = [(C(i+1,j-1:j)=='#'),0];
            elseif i==1
                oc1 = [0,0,0];
                oc2 = (C(i,j-1:j+1)=='#'); oc2(1,2)=0;
                oc3 = (C(i+1,j-1:j+1)=='#');
            elseif (i==s2(1,1))&&(j==1)
                oc1 = [0,(C(i-1,j:j+1)=='#')];
                oc2 = [0,0,(C(i,j+1)=='#')];
                oc3 = [0,0,0];
            elseif (i==s2(1,1))&&(j==s2(1,2))
                oc1 = [(C(i-1,j-1:j)=='#'),0];
                oc2 = [(C(i,j-1)=='#'),0,0];
                oc3 = [0,0,0];
            elseif i==s2(1,1)
                oc1 = (C(i-1,j-1:j+1)=='#');
                oc2 = (C(i,j-1:j+1)=='#'); oc2(1,2)=0;
                oc3 = [0,0,0];
            elseif j==1
                oc1 = [0,(C(i-1,j:j+1)=='#')];
                oc2 = [0,0,(C(i,j+1)=='#')]; 
                oc3 = [0,(C(i+1,j:j+1)=='#')];
            elseif j==s2(1,2)
                oc1 = [(C(i-1,j-1:j)=='#'),0];
                oc2 = [(C(i,j-1)=='#'),0,0];
                oc3 = [(C(i+1,j-1:j)=='#'),0];
            else
                oc1 = (C(i-1,j-1:j+1)=='#');
                oc2 = (C(i,j-1:j+1)=='#'); oc2(1,2)=0;
                oc3 = (C(i+1,j-1:j+1)=='#');
            end
            suma = sum([oc1,oc2,oc3]);
            if (C(i,j)=='L')&&(suma==0)
                B(i,j) = '#';
            elseif (C(i,j)=='#')&&(suma>=4)
                B(i,j) = 'L';
            end
            
        end
        
    end
    if B==C
        this_no = no
        break
    end
    
end

sum(sum(B=='#'))

toc


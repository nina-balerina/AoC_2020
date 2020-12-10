fid = fopen('day3.txt','r');
S = textscan(fid, '%s');
fclose = (fid);
A = S{1};
s1 = size(A);

for i=1:1:s1(1,1)
    B = A{i};
    s = size(B);
    C(i,1:s(1,2))=B;
end

np1(1)=1; np2(1)=1; np5(1)=1; np7(1)=1; np9(1)=1; np10(1)=1;
zbroj_3_1=0; zbroj_1_1=0; zbroj_5_1=0; zbroj_7_1=0; zbroj_1_2=0;

for i=2:1:s1(1,1)
    
    % right3, down 1
    np1(i)=i;   np2(i)=np2(i-1)+3;  np4(i)=mod(np2(i),s(1,2));
        if np4(i)==0
            ch=C(np1(i),s(1,2));
        else
            ch=C(np1(i),np4(i));
        end
        if ch=='#'
            zbroj_3_1=zbroj_3_1+1;
        end
    
    % right1, down1
    np3(i)=mod(np1(i),s(1,2));
        if mod(np1(i),s(1,2))==0
            ch=C(np1(i),s(1,2));
        else
            ch=C(np1(i),np3(i));
        end
        if ch=='#'
            zbroj_1_1=zbroj_1_1+1;
        end
    
    % right5, down1
    np5(i)=np5(i-1)+5;  np6(i)=mod(np5(i),31);
        if mod(np6(i),31)==0
            ch=C(np1(i),s(1,2));
        else
            ch=C(np1(i),np6(i));
        end
        if ch=='#'
            zbroj_5_1=zbroj_5_1+1;
        end
    
    % right7, down1
    np7(i)=np7(i-1)+7;  np8(i)=mod(np7(i),s(1,2));
        if mod(np8(i),s(1,2))==0
            ch=C(np1(i),s(1,2));
        else
            ch=C(np1(i),np8(i));
        end
        if ch=='#'
            zbroj_7_1=zbroj_7_1+1;
        end
    
    % right1, down2
    if mod(i,2)==1
        np9(i)=np9(i-2)+2;  np10(i)=np10(i-2)+1;   np11(i)=mod(np10(i),s(1,2));
            if mod(np11(i),s(1,2))==0
                ch=C(np9(i),s(1,2));
            else
                ch=C(np1(i),np11(i));
            end
            if ch=='#'
                zbroj_1_2=zbroj_1_2+1;
            end
    end
    
end

part1=zbroj_3_1

part2=zbroj_1_1*zbroj_1_2*zbroj_3_1*zbroj_5_1*zbroj_7_1

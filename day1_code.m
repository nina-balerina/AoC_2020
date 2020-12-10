fid = fopen('day1.txt','r');
S = textscan(fid, '%d');
fclose(fid);

input = S{1};

for i = 1:1:200
    for j = i+1:1:200
        sum1(i,j) = input(i,1) + input (j,1);
        if sum1(i,j) == 2020
            br1 = i;
            br2 = j;
            multi1 = input(i,1) * input(j,1);
        end
    end
end

for i = 1:1:200
    for j = i+1:1:200
        for k = j+1:1:200
            sum2(i,j,k) = input(i,1) + input (j,1) + input(k,1);
            if sum2(i,j,k) == 2020
                br3 = i;
                br4 = j;
                br5 = k;
                multi2 = input(i,1) * input(j,1) * input(k,1);
            end
        end
    end
end




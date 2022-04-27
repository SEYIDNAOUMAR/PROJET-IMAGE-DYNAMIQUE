
function B=photomaton(A,n)
    B=zeros(n);
    for i=1:n
        for j=1:n
        wi=photomatIndice(i,n);
        wj=photomatIndice(j,n);
        B(wi,wj)=A(i,j);
        end
    end
end



//https://www.codechef.com/problems/LECANDY
#include <iostream>
using namespace std;

int main() {
    long sum,c,n;
	int t,k;
	cin>>t;
	while (t--)
	{
	    cin>>n>>c;
	    sum=0;
	    for(int i=0;i<n;i++)
		{
			cin>>k;
			sum+=k;
		}
		if(sum<=c)
			cout<<"Yes\n";
		else
			cout<<"No\n";
	}
	return 0;
}

#include <iostream>
using namespace std;

void maxk(int arr[],int k,int n)
{
    int max_el = arr[0];
    int max_idx = 0;
    for(int i=0;i<k;i++)
    {
        if (max_el<arr[i])
        {
            max_el=arr[i];
            max_idx = i;
        }
    }
    int start_idx=0;
    for(int ctr=k;ctr<=n;ctr++,start_idx++)
    {
        // cout<<"its at"<<ctr<<" ";
        // if the next element is bigger than the running max
        if(max_el<arr[ctr-1])
        {
            max_el=arr[ctr-1];
            max_idx=ctr-1;
        }
        else
        {
            cout<<"max"<<max_idx<<" "<<ctr-k<<endl;
            // if the last max is outside the window
            if(start_idx>max_idx)
            {
                max_el=arr[ctr-k];
                max_idx=ctr-k;
                // cout<<"checing"<<" "<<max_el;
                int j=start_idx;
                // cout<<"starting at"<<j<<endl;
                while(j<ctr && j<n)
                {
                    // cout<<j<<endl;
                    if(max_el<arr[j])
                    {
                        // cout<<"increase"<<arr[j]<<" "<<j;
                        max_el=arr[j];
                        max_idx=j;
                    }
                    j++;
                }
                
            }
        }
        cout<<max_el<<" ";
    }
    cout<<"\n";
}
int main() {
	//code
	int tests;
	cin>>tests;
	while(tests>0)
    	{
    	    int size, k;
        	cin>>size>>k;
        	int arr[size];
        	int ctr=0;
        	while(ctr<size)
        	{
        	    int a;
        	    cin>>a;
        	   // cout<<ctr<<" "<<a<<endl;
        	    arr[ctr]=a;
        	    ctr++;
        	}
        	maxk(arr,k,size);
        	tests--;
    	    
    	}
	
	return 0;
}
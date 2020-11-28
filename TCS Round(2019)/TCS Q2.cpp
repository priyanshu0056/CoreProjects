//TCS Q2 Choclate Distribution
#include<iostream>
using namespace std;
int max(int l,int b)
{
 if(l>b)
   return l;
 else
 return b;
}
int min(int l,int b)
{
 if(l<b)
   return l;
  else
    return b;
      }
int chocolate(int l,int b)
{
  int lon,sh,diff,count=0;
  while(1)
  {
    lon=max(l,b);
    sh=min(l,b);
    count++;
    diff=lon-sh;
    if(diff==0)
      return count;
    else
    {
      l=min(l,b);
        b=diff;
    }
    }

}

int main()
{
  int minl,maxl,minb,maxb,i,j;
  cout<<"Enter"<<endl;
  cin>>minl>>maxl>>minb>>maxb;
   int total=0;
 for(i=minl;i<=maxl;i++)
    for(j=minb;j<=maxb;j++)
          total+=chocolate(i,j);
  cout<<total;
}
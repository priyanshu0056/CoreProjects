//Bride & Groom Question Appear in TCS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void shiftleft(char* string,int shiftlen)
{
    int i,size=strlen(string);
    if(shiftlen>=size)
    {
    memset(string,'\0',size);
    return;
    }
        for(i = 0; i < size-shiftlen; i++)
        {
            string[i]=string[i+shiftlen];
            string[i+shiftlen]='\0';
        }
}
void RemoveChars(char *s, char c)
{
    int writer = 0, reader = 0;

    while (s[reader])
    {
        if (s[reader]!=c) 
        {   
            s[writer++] = s[reader];
        }

        reader++;       
    }

    s[writer]=0;
}

int main()
{ 
int N;
printf("Enter value of N=");
scanf("%d",&N);
char s1[10000],s2[10000];
 printf("\nEnter Bride drink=");
 scanf("%s",s1);
 printf("\nEnter Groom drink=");
 scanf("%s",s2);
 
for(int i = 0; i < N; i++)
{
    if (s1[i]==s2[i])
    {
        RemoveChars(s1,s1[i]);
        RemoveChars(s2,s2[i]);
    
    }
    else
    {
    shiftleft(s1,1);  
    
    }
}
if (s1=='\0'&&s2=='\0')
{
    printf("\nOutput is 0");
}
else
{
    printf("\nOutput is Null if all are sorted  :%s %s",s1,s2);
}
return 0;
}
#include<iostream>
#include<map>
#include<iterator>
#include<algorithm>
#include<vector>

using namespace std;
int main(int argc,char *argv[]){
    map<string,int> imap;
    imap["name"]=5;
    imap["age"]=13;
    imap.insert(make_pair("hello",6));
    for(auto iter=imap.begin();iter!=imap.end();++iter){
        pair<string,int> itemp=*iter;
        cout<<itemp.first<<" "<<itemp.second<<endl;
    }
    vector<int> ivec;
    ivec.push_back(2);
    ivec.push_back(1);
    ivec.push_back(6);
    ivec.push_back(5);
    sort(ivec.begin(),ivec.end(),[](int a,int b) {return a>b;});
    for(auto iter=ivec.begin();iter!=ivec.end();++iter){
        cout<<*iter<<"  ";
    }
    
}
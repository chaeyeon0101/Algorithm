#include <bits/stdc++.h>
using namespace std;
int arr[50][50];

int dx[]={-1, 1, 0, 0};
int dy[]={0, 0, 1, -1};

void bfs(int m, int n, int x, int y){
    queue<pair<int, int>> q;
    q.push({x, y});
    arr[x][y] = 0;
    
    while(!q.empty()){
        x = q.front().first;
        y = q.front().second;
        q.pop();
        
        for(int i=0;i<4;i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx<0 || nx>=m || ny<0 || ny>=n) continue;
            if(arr[nx][ny]==1){
                q.push({nx, ny});
                arr[nx][ny] = 0;
            }
        }
    }
}

int main(){
    int t;
    cin>>t;
    
    while(t > 0){
        memset(arr, 0, sizeof(arr));
        
        int m, n, k;
        cin>>m>>n>>k;
        
        for(int i=0;i<k;i++){
            int a,b;
            cin>>a>>b;
            arr[a][b]=1;
        }
        
        int answer=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(arr[i][j]==1){
                    bfs(m, n, i, j);
                    answer++;
                }
            }
        }
        
        cout<<answer<<endl;
        t--;
    }
    
    return 0;
}
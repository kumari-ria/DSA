// There are flight paths between cities. If there is a flight between city A and city B then 
// there is an edge between the cities. The cost of the edge can be the time that flight take 
// to reach city B from A, or the amount of fuel used for the journey. Represent this as a 
// graph. The node can be represented by airport name or name of the city. Use adjacency 
// list representation of the graph or use adjacency matrix representation of the graph. 
// Check whether the graph is connected or not. Justify the storage representation used

#include <iostream>
#include <stack>
#include <queue>
using namespace std;

class Graph
{
    string city[10];
    int a[10][10];
    int n;
    public:
    void getdata();
    void display();
    void BFS();
    void DFS();
};
void Graph :: getdata()
{
    cout<<"enter the number of cites";
    cin>>n;
    cout<<"enter the names of cities";
    for(int i=0;i<n;i++)
    {
        cin>>city[i];
    }
    cout<<"enter the distance btw cities";
    for (int i =0;i<n;i++)
    {
        for (int j=0;j<n;j++)
        {
            cout<<"enter the distance between "<<city[i]<<" and "<<city[j]<<endl;
            cin>>a[i][j];
        }
    }
}
void Graph :: display()
{
    for (int i =0;i<n;i++)
    {
        for (int j=0;j<n;j++)
        {
            cout<<a[i][j]<<" ";
        }
        cout<<endl;
    }
}

int main()
{
    Graph g;
    g.getdata();
    g.display();
    return 0;
}
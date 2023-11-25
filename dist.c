#include <stdio.h>
struct node
{
    int dist[20];
    int from[20];
} rt[10];

int main()
{
    int n, i, j, k, count = 1;
    int dmat[20][20];

    printf("\nenter the number of nodes\n");
    scanf("%d", &n);
    printf("\nenter the cost matrix\n");
    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++)
        {
            scanf("%d", &dmat[i][j]);
            dmat[i][i] = 0;
            rt[i].dist[j] = dmat[i][j];
            rt[i].from[j] = j;
        }
    do
    {
        for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
                for (k = 1; k <= n; k++)
                    if (rt[i].dist[j] > dmat[i][k] + rt[k].dist[j])
                    {
                        rt[i].dist[j] = rt[i].dist[k] + rt[k].dist[j];
                        rt[i].from[j] = k;
                    }

        count++;

    } while (count < n);

    for (i = 1; i <= n; i++)
    {
        printf("\nthe distance vector table for %c is\n", i + 64);
        for (j = 1; j <= n; j++)
            printf("\tNode is %c via%c distance is %d\n", j + 64, rt[i].from[j] + 64, rt[i].dist[j]);
    }
    return 0;
}
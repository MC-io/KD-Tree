#include <iostream>
#include "KDTree.h"

int main()
{
    KDTree<3> arbolitooo;
    arbolitooo.insert({10,0,100});
    arbolitooo.insert({5,10,15});
    arbolitooo.insert({7,7,7});
    arbolitooo.insert({9,0,0});
    arbolitooo.insert({11,10,9});
    arbolitooo.insert({11,0,0});

    arbolitooo.print_pre_order();
}
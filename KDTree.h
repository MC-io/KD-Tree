#ifndef __KD_TREE_H__
#define __KD_TREE_H__

#include "Node.h"
#include <iostream>

template <int T>
class KDTree
{
private:
    Node<T> * root;
    int size;
public:
    KDTree();
    void insert(std::vector<int> vec);
    void print_pre_order(Node<T> * node);
    void print_pre_order();
};

template <int T>
KDTree<T>::KDTree()
{
    this->root = nullptr;
    this->size = 0;
}

template <int T>
void KDTree<T>::insert(std::vector<int> vec)
{
    if (!this->root)
    {
        this->root = new Node<T>(vec);
        size++;
        return;
    }

    Node<T> * new_node = new Node<T>(vec);
    Node<T> * tmp = this->root;
    Node<T> * tmp2 = tmp;

    int height = 0;
    
    while(tmp != nullptr)
    {
        tmp2 = tmp;
        if (tmp->vec[height % T] > new_node->vec[height % T])
        {
            tmp = tmp->left;
        }
        else tmp = tmp->right;
        height++;
    }
    height--;

    if (tmp2->vec[height % T] > new_node->vec[height % T])
    {
        tmp2->left = new_node;
    }
    else tmp2->right = new_node;
    size++;
}

template <int T>
void KDTree<T>::print_pre_order(Node<T> * node)
{
    if (!node) return;
    this->print_pre_order(node->left);
    for (int i = 0; i < T; i++)
    {
        std::cout << node->vec[i] << ' ';
    }
    std::cout << '\n';
    this->print_pre_order(node->right);
}


template <int T>
void KDTree<T>::print_pre_order()
{
    this->print_pre_order(this->root);
}
#endif  // __KD_TREE_H__
#ifndef __NODE_H__
#define __NODE_H__

#include <iostream>
#include <vector>

template <int T>
class KDTree;

template <int T>
class Node
{
private:
    std::vector<int> vec;
    int height;
    Node<T> * left;
    Node<T> * right;
    friend class KDTree<T>;
public:
    std::vector<int> get_vec();
    Node(const std::vector<int> vec);
    void set_height(int height);

};

template <int T>
Node<T>::Node(const std::vector<int> vec)
{
    this->vec = vec;
    this->left = this->right = nullptr;
}

template <int T>
std::vector<int> Node<T>::get_vec()
{
    return this->vec;
}

template <int T>
void Node<T>::set_height(int height)
{
    this->height = height;
}


#endif  // __NODE_H__
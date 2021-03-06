#include <stdio.h>
using namespace std;

enum class shape_type
{
    circle,
    triangle,
    rectangle,
};

class shape {};
class circle : public shape {};
class triangle : public shape {};
class rectangle : public shape {};

shape * create_shape(shape_type type)
{
    switch (type)
    {
    case shape_type::circle:
        return new circle();
    case shape_type::triangle:
        return new triangle();
    case shape_type::rectangle:
        return new rectangle();
    default:
        return nullptr;
    }
}

class shape_wrapper
{
public:
    explicit shape_wrapper(shape *ptr = nullptr) : ptr_(ptr) {}
    ~shape_wrapper()
    {
        delete ptr_;
    }

    shape *get() const { return ptr_; }

private:
    shape * ptr_;
};

void foo()
{
    shape_wrapper ptr_wrapper(create_shape(shape_type::circle));
}



// class Obj
// {
// public:
//     Obj() { puts("Obj()"); }
//     ~Obj() { puts("~Obj()"); }
// };

// void foo(int n)
// {
//     Obj obj;
//     if (n == 42)
//         throw "life, the universe and everthing";
// }

// int main()
// {
//     try
//     {
//         foo(41);
//         foo(42);
//     }
//     catch(const char* s)
//     {
//         puts(s);
//     }
//     return 0;
// }



// class bar
// {
// };

// bar *make_bar()
// {
//     bar *ptr = nullptr;
//     try
//     {
//         ptr = new bar();
//     }
//     catch (...)
//     {
//         delete ptr;
//         throw;
//     }
//     return ptr;
// }

// void foo(int n)
// {
//     bar *ptr = make_bar();

//     delete ptr;
// }
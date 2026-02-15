#ifndef PROJECT_MODULE1_H
#define PROJECT_MODULE1_H


// System includes
#include <string>

// Project includes


namespace project {


/// @brief Class description
class Module1 :
    public base::BaseModule,
    virtual public interfaces::IRuntime,
    virtual public interfaces::IModuleType1
{
// -- Constructors & Destructor --
public:

    /// @brief Constructor description
    Module1();

    /// @brief Destructor of Module1
    ~Module1() noexcept;

// -- Members --
public:

    /// @brief Member description
    std::string name;

protected:

private:

    /// @brief Member description
    int id;

// -- Methods --
public:

    /// @brief Method description
    void Start();

protected:

    /// @brief Method description
    /// @param new_name Param description
    /// @param flag Param description
    const void SetName(const std::string &new_name, int flag) const noexcept override;

private:

}; // class Module1


} // namespace project


#endif // PROJECT_MODULE1_H

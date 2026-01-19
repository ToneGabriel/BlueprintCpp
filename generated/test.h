#ifndef INTERFACES_MODULE_MODULE1_H
#define INTERFACES_MODULE_MODULE1_H


// System includes
#include <string>

// Project includes
#include "base/BaseModule"
#include "interfaces/IRuntime"
#include "interfaces/IModuleType1"


namespace interfaces {
namespace module {


/// @brief None
class Module1
    : public base::BaseModule
    , public interfaces::IRuntime
    , public interfaces::IModuleType1
{
// -- Constructors & Destructor --
public:

    /// @brief Default constructor description
    Module1();

    /// @brief Constructor description
    /// @param new_name Param description
    /// @param flag Param description
    Module1(const std::string& new_name, int flag) noexcept;

    /// @brief Destructor description
    virtual ~Module1() noexcept = 0;

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
    virtual void SetName(const std::string& new_name, int flag) const noexcept override = 0;

private:

}; // class Module1


} // namespace module
} // namespace interfaces


#endif // INTERFACES_MODULE_MODULE1_H

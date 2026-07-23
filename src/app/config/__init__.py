
GENERATOR_APP_NAME: str = "BlueprintCPP"

JINJA_ENV_PACKAGE: str                  = "app.jinja"
CLASS_HEADER_TEMPLATE_FILENAME: str     = "class.h.j2"
CLASS_SOURCE_TEMPLATE_FILENAME: str     = "class.cpp.j2"
INTERFACE_HEADER_TEMPLATE_FILENAME: str = "interface.h.j2"
ENUM_HEADER_TEMPLATE_FILENAME: str      = "enum.h.j2"
TAB_INDENT: str                         = "    "


STANDARD_INCLUDE_MAP: dict[str, str] = {
    # Containers
    "std::array":               "array",
    "std::deque":               "deque",
    "std::forward_list":        "forward_list",
    "std::list":                "list",
    "std::map":                 "map",
    "std::multimap":            "map",
    "std::multiset":            "set",
    "std::set":                 "set",
    "std::unordered_map":       "unordered_map",
    "std::unordered_multimap":  "unordered_map",
    "std::unordered_set":       "unordered_set",
    "std::unordered_multiset":  "unordered_set",
    "std::vector":              "vector",
    "std::stack":               "stack",
    "std::queue":               "queue",
    "std::priority_queue":      "queue",

    # Strings
    "std::string":              "string",
    "std::wstring":             "string",
    "std::u8string":            "string",
    "std::u16string":           "string",
    "std::u32string":           "string",
    "std::string_view":         "string_view",
    "std::wstring_view":        "string_view",

    # Smart pointers
    "std::unique_ptr":          "memory",
    "std::shared_ptr":          "memory",
    "std::weak_ptr":            "memory",
    "std::make_unique":         "memory",
    "std::make_shared":         "memory",

    # Utilities
    "std::pair":                "utility",
    "std::tuple":               "tuple",
    "std::optional":            "optional",
    "std::variant":             "variant",
    "std::any":                 "any",
    "std::function":            "functional",
    "std::reference_wrapper":   "functional",
    "std::move":                "utility",
    "std::forward":             "utility",
    "std::swap":                "utility",

    # Algorithms / numerics
    "std::accumulate":          "numeric",
    "std::reduce":              "numeric",
    "std::transform":           "algorithm",
    "std::find":                "algorithm",
    "std::sort":                "algorithm",

    # Iterators
    "std::iterator":            "iterator",
    "std::back_inserter":       "iterator",
    "std::inserter":            "iterator",

    # Streams
    "std::istream":             "istream",
    "std::ostream":             "ostream",
    "std::ifstream":            "fstream",
    "std::ofstream":            "fstream",
    "std::stringstream":        "sstream",
    "std::istringstream":       "sstream",
    "std::ostringstream":       "sstream",
    "std::cout":                "iostream",
    "std::cin":                 "iostream",
    "std::cerr":                "iostream",

    # Threads / concurrency
    "std::thread":              "thread",
    "std::mutex":               "mutex",
    "std::recursive_mutex":     "mutex",
    "std::lock_guard":          "mutex",
    "std::unique_lock":         "mutex",
    "std::scoped_lock":         "mutex",
    "std::condition_variable":  "condition_variable",
    "std::future":              "future",
    "std::promise":             "future",
    "std::async":               "future",
    "std::atomic":              "atomic",

    # Type traits
    "std::enable_if":           "type_traits",
    "std::is_same":             "type_traits",
    "std::is_base_of":          "type_traits",
    "std::remove_reference":    "type_traits",
    "std::decay":               "type_traits",

    # Error handling
    "std::exception":           "exception",
    "std::runtime_error":       "stdexcept",
    "std::logic_error":         "stdexcept",
    "std::error_code":          "system_error",

    # Misc
    "std::filesystem::path":    "filesystem",
    "std::span":                "span",
    "std::bitset":              "bitset",
    "std::regex":               "regex",
    "std::initializer_list":    "initializer_list",
    "std::clamp":               "algorithm",

    # Time
    "std::chrono::duration":        "chrono",
    "std::chrono::time_point":      "chrono",
    "std::chrono::system_clock":    "chrono",
    "std::chrono::steady_clock":    "chrono",

    # Random
    "std::mt19937":                     "random",
    "std::uniform_int_distribution":    "random",
    "std::uniform_real_distribution":   "random",
    "std::random_device":               "random"
}

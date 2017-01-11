import cffi

ffibuilder = cffi.FFI()
ffibuilder.set_source("_stringmatch", r"""
#include <string.h>
#include <string>

struct MatchResult {
    int start_pos;
    int end_pos;
    int cost;
};

MatchResult match(const char* a, const char* b) {
 //Noah's code here
  const int a_len = strlen(a);
  const int b_len = strlen(b);
  MatchResult m;
  m.start_pos = 0;
  m.end_pos = 0;
  m.cost = 100;
  return m;
}
""",
source_extension='.cpp',
)

ffibuilder.cdef("""
typedef struct {
    int start_pos;
    int end_pos;
    int cost;
} MatchResult;
MatchResult match(const char* a, const char* b);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

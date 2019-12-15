/*
 * Wrappers to emulate dlopen() on other systems like Windows
 */

#include "wraphelper.h"

#if defined(_WIN32)
void* wrap_dlopen(const char* filename)
{
    return (void*)LoadLibrary(filename);
}
void* wrap_dlsym(void* h, const char* sym)
{
    return (void*)GetProcAddress((HINSTANCE)h, sym);
}
int wrap_dlclose(void* h)
{
    /* FreeLibrary returns non-zero on success */
    return (!FreeLibrary((HINSTANCE)h));
}
#else
/* assume we can use dlopen itself... */
void* wrap_dlopen(const char* filename)
{
    return dlopen(filename, RTLD_NOW);
}
void* wrap_dlsym(void* h, const char* sym)
{
    return dlsym(h, sym);
}
int wrap_dlclose(void* h)
{
    return dlclose(h);
}
#endif

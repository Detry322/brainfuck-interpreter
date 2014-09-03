#ifndef DATA_STRIP
#define DATA_STRIP

//structs
struct data_strip_node {
	data_strip_node prev;
	data_strip_node next;
	char value;
};
typedef struct data_strip_node* data_strip_node;

struct data_strip {
	data_strip_node current;
};
typedef struct data_strip* data_strip;

// ------------------

//functions
data_strip ds_create(void);
int ds_next(data_strip strip);
int ds_prev(data_strip strip);
void ds_increment(data_strip strip);
void ds_decrement(data_strip strip);
char ds_val(data_strip strip);

#endif

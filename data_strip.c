#include "data_strip.h"

data_strip ds_create(void) {
	data_strip strip = malloc(sizeof(struct data_strip));
	strip->current = ds_create_node();
	return strip;
}

static data_strip_node ds_create_node(void) {
	data_strip_node node = malloc(sizeof(struct data_strip_node))
	node->value = 0;
	node->next = NULL;
	node->prev = NULL;
	return node;
}

int ds_next(data_strip strip) {
	if (strip->current->next) {
		strip->current = strip->current->next;
		return 0;
	}
	strip->current->next = ds_create_node();
	strip->current->next->prev = strip->current;
	return ds_next(strip) + 1;
}

int ds_prev(data_strip strip) {
	if (strip->current->prev) {
		strip->current = strip->current->prev;
		return 0;
	}
	strip->current->prev = ds_create_node();
	strip->current->prev->next = strip->current;
	return ds_prev(strip) + 1;
}

void ds_increment(data_strip strip) {
	strip->current->value++;
}

void ds_decrement(data_strip strip) {
	strip->current->value--;
}

char ds_val(data_strip strip) {
	return strip->current->value;
}

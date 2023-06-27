#pragma once

struct Node{
	int x, y;
	int side = 16;

	Node() {}
	
	bool isInArea(int mouseX, int mouseY){
		return mouseX >= x && mouseX <= x+side && mouseY >= y && mouseY <=y+side;
	}
};
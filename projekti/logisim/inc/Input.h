#include <bits/stdc++.h>
#include <SDL2/SDL.h>
#include "Node.h"

unsigned int nn=0;

class Input{
private:
	int x, y;
	const int size=64;
	Node out;
	
	SDL_Rect rect = {x, y, size, size};
	
public:
	int id;
	bool state;
	static std::vector<Input*> inputs;
	static std::vector<Input*>& getInputs() {return inputs;}

	Input(int xx, int yy, bool st)
        : x(xx), y(yy), state(st) { 
        inputs.push_back(this);
        this->id = nn;
        ++nn;
        out.x=this->x+this->size-8;
        out.y=this->y+this->size/2-8;
    }

	void renderBase(SDL_Renderer* renderer, int r, int g, int b) {
        out.x = this->x + this->size - 8;
        out.y = this->y + this->size/2 - 8;
        SDL_Rect outputL = {out.x, out.y, 16, 16};
        SDL_Rect outputF = {out.x+1, out.y+1, 16-2, 16-2};
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderDrawRect(renderer, &outputL);
        SDL_SetRenderDrawColor(renderer, r, g, b, 255);
        SDL_RenderFillRect(renderer, &outputF);
    }
	void render(SDL_Renderer* renderer, int r, int g, int b){
        
        renderBase(renderer, r, g, b);
    }
    //void postRender(SDL_Renderer* renderer, int r, int g, int b){
    //    SDL_SetRenderDrawColor(renderer, r, g, b, 255);
    //    SDL_Rect outputF = {out.x+1, out.y+1, this->size-2, this->size-2};
    //    SDL_RenderFillRect(renderer, &outputF);
    //}


    int getX() const {return this->x;}
    int getY() const {return this->y;}
    int getSize() const {return this->size;}
    Node& getOutputNode() {return out;}

    void setX(const int x) {this->x=x;}
    void setY(const int y) {this->y=y;}
    void setXY(const int x, const int y) {
    	this->x = x;
    	this->y = y;
    }
    void addXY(const int x, const int y) {
    	this->x += x;
    	this->y += y;
    }
};

inline void initializeIO(SDL_Renderer* renderer){
    
}
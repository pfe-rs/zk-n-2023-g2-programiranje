#include <bits/stdc++.h>
#include <SDL2/SDL.h>
#include "Node.h"

unsigned int num=0;

class Gate{
protected:
	int x, y;
	const int wsize=128, hsize=64;
	const int side=16;
	Node outputNode;
	Node inA, inB;
	
	std::vector<bool> in;
	SDL_Rect rect = {x, y, wsize, hsize};

	Gate(int xx, int yy)
		: x(xx), y(yy) { 
        objects.push_back(this);
        this->id = num;
        ++num;
        outputNode.x=this->x+this->wsize-8;
        outputNode.y=this->y+this->hsize/2-8;
    }
	
public:
	int id;
	static std::vector<Gate*> objects;
	static std::vector<Gate*>& getObjects() {return objects;}

	Gate() {}

	virtual bool evaluate() const = 0;
	virtual void render(SDL_Renderer* renderer, int r, int g, int b) = 0;

	void renderBase(SDL_Renderer* renderer, int r, int g, int b) {
        inA.x = this->x - 8;
        inA.y = this->y + 8;
        inB.x = this->x - 8;
        inB.y = this->y + 40;
        outputNode.x = this->x + this->wsize - 8;
        outputNode.y = this->y + this->hsize/2 - 8;
        SDL_Rect inAL = {inA.x, inA.y, side, side};
        SDL_Rect inAF = {inA.x+1, inA.y+1, side-2, side-2};
        SDL_Rect inBL = {inB.x, inB.y, side, side};
        SDL_Rect inBF = {inB.x+1, inB.y+1, side-2, side-2};
        SDL_Rect outputL = {outputNode.x, outputNode.y, side, side};
        SDL_Rect outputF = {outputNode.x+1, outputNode.y+1, side-2, side-2};
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderDrawRect(renderer, &inAL);
        SDL_RenderDrawRect(renderer, &inBL);
        SDL_RenderDrawRect(renderer, &outputL);
        SDL_SetRenderDrawColor(renderer, r, g, b, 255);
        SDL_RenderFillRect(renderer, &inAF);
        SDL_RenderFillRect(renderer, &inBF);
        SDL_RenderFillRect(renderer, &outputF);
    }
	
    bool operator[](int index){
    	ASSERT(0<=index && index<this->in.size(), "Invalid index range when called inputs");
    	return this->in[index];
    }
    void postRender(SDL_Renderer* renderer, int state, int r, int g, int b){
    	SDL_SetRenderDrawColor(renderer, r, g, b, 255);
    	if(state==0){
    		SDL_Rect inAF = {inA.x+1, inA.y+1, side-2, side-2};
    		SDL_RenderFillRect(renderer, &inAF);
    	}
    	if(state==1){
    		SDL_Rect inBF = {inB.x+1, inB.y+1, side-2, side-2};
        	SDL_RenderFillRect(renderer, &inBF);
    	}
    	if(state==2){
    		SDL_Rect outputF = {outputNode.x+1, outputNode.y+1, side-2, side-2};
    		SDL_RenderFillRect(renderer, &outputF);
    	}
    }

    int getX() const {return this->x;}
    int getY() const {return this->y;}
    int getW() const {return this->wsize;}
    int getH() const {return this->hsize;}
    Node& getOutputNode() {return outputNode;}
    Node& getInA() {return inA;}
	Node& getInB() {return inB;}

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


class ANDGate : public Gate {
public:
	static SDL_Texture* texture;

	ANDGate() {}
	ANDGate(int x, int y)
		: Gate(x, y) {objects.push_back(this); this->id = num; ++num; in.resize(2, 0);}


	static void initialize(SDL_Renderer* renderer, const char* path) {
			
		SDL_Surface* img = SDL_LoadBMP(path);
		texture = SDL_CreateTextureFromSurface(renderer, img);
	}

	bool evaluate() const override {
		return in[0]&in[1];
	}
	void render(SDL_Renderer* renderer, int r, int g, int b) override {
		this->rect = {x, y, wsize, hsize};
		SDL_RenderCopy(renderer, texture, NULL, &rect);
		renderBase(renderer, r, g, b);
	}
};
SDL_Texture* ANDGate::texture = NULL;	

class NANDGate : public Gate {
public:
	static SDL_Texture* texture;

	NANDGate() {}
	NANDGate(int x, int y)
		: Gate(x, y) {objects.push_back(this); this->id = num; ++num; in.resize(2, 0);}

	
	static void initialize(SDL_Renderer* renderer, const char* path) {
			
		SDL_Surface* img = SDL_LoadBMP(path);
		texture = SDL_CreateTextureFromSurface(renderer, img);
	}

	virtual bool evaluate() const override {
		return !(in[0]&in[1]);
	}
	void render(SDL_Renderer* renderer, int r, int g, int b) override {
		this->rect = {x, y, wsize, hsize};
		SDL_RenderCopy(renderer, texture, NULL, &rect);
		renderBase(renderer, r, g, b);
	}
};
SDL_Texture* NANDGate::texture = NULL;

class ORGate : public Gate {
public:
	static SDL_Texture* texture;

	ORGate() {}
	ORGate(int x, int y)
		: Gate(x, y) {objects.push_back(this); this->id = num; ++num; in.resize(2, 0);}

	
	static void initialize(SDL_Renderer* renderer, const char* path) {
			
		SDL_Surface* img = SDL_LoadBMP(path);
		texture = SDL_CreateTextureFromSurface(renderer, img);
	}

	virtual bool evaluate() const override {
		return in[0]|in[1];
	}
	void render(SDL_Renderer* renderer, int r, int g, int b) override {
		this->rect = {x, y, wsize, hsize};
		SDL_RenderCopy(renderer, texture, NULL, &rect);
		renderBase(renderer, r, g, b);
	}
};
SDL_Texture* ORGate::texture = NULL;

class NORGate : public Gate {
public:
	static SDL_Texture* texture;

	NORGate() {}
	NORGate(int x, int y)
		: Gate(x, y) {objects.push_back(this); this->id = num; ++num; in.resize(2, 0);}

	
	static void initialize(SDL_Renderer* renderer, const char* path) {
			
		SDL_Surface* img = SDL_LoadBMP(path);
		texture = SDL_CreateTextureFromSurface(renderer, img);
	}

	virtual bool evaluate() const override {
		return !(in[0]|in[1]);
	}
	void render(SDL_Renderer* renderer, int r, int g, int b) override {
		this->rect = {x, y, wsize, hsize};
		SDL_RenderCopy(renderer, texture, NULL, &rect);
		renderBase(renderer, r, g, b);
	}
};
SDL_Texture* NORGate::texture = NULL;

class XORGate : public Gate {
public:
	static SDL_Texture* texture;

	XORGate() {}
	XORGate(int x, int y)
		: Gate(x, y) {objects.push_back(this); this->id = num; ++num; in.resize(2, 0);}


	static void initialize(SDL_Renderer* renderer, const char* path) {
			
		SDL_Surface* img = SDL_LoadBMP(path);
		texture = SDL_CreateTextureFromSurface(renderer, img);
	}

	bool evaluate() const override {
		return in[0]^in[1];
	}
	void render(SDL_Renderer* renderer, int r, int g, int b) override {
		this->rect = {x, y, wsize, hsize};
		SDL_RenderCopy(renderer, texture, NULL, &rect);
		renderBase(renderer, r, g, b);
	}
};
SDL_Texture* XORGate::texture = NULL;

class NXORGate : public Gate {
public:
	static SDL_Texture* texture;

	NXORGate() {}
	NXORGate(int x, int y)
		: Gate(x, y) {objects.push_back(this); this->id = num; ++num; in.resize(2, 0);}


	static void initialize(SDL_Renderer* renderer, const char* path) {
			
		SDL_Surface* img = SDL_LoadBMP(path);
		texture = SDL_CreateTextureFromSurface(renderer, img);
	}

	bool evaluate() const override {
		return !(in[0]^in[1]);
	}
	void render(SDL_Renderer* renderer, int r, int g, int b) override {
		this->rect = {x, y, wsize, hsize};
		SDL_RenderCopy(renderer, texture, NULL, &rect);
		renderBase(renderer, r, g, b);
	}
};		
SDL_Texture* NXORGate::texture = NULL;

class NOTGate : public Gate {
public:
	static SDL_Texture* texture;

	NOTGate() {}
	NOTGate(int x, int y)
		: Gate(x, y) {objects.push_back(this); this->id = num; ++num; in.resize(1, 0);}


	static void initialize(SDL_Renderer* renderer, const char* path) {
			
		SDL_Surface* img = SDL_LoadBMP(path);
		texture = SDL_CreateTextureFromSurface(renderer, img);
	}

	bool evaluate() const override {
		return !in[0];
	}
	void render(SDL_Renderer* renderer, int r, int g, int b) override {
		this->rect = {x, y, wsize, hsize};
		SDL_RenderCopy(renderer, texture, NULL, &rect);
		renderBase(renderer, r, g, b);
	}
};
SDL_Texture* NOTGate::texture = NULL;

static void initializeGates(SDL_Renderer* renderer){
	ANDGate::initialize(renderer, "img/AND.bmp");
	NANDGate::initialize(renderer, "img/NAND.bmp");
	ORGate::initialize(renderer, "img/OR.bmp");
	NORGate::initialize(renderer, "img/NOR.bmp");
	XORGate::initialize(renderer, "img/XOR.bmp");
	NXORGate::initialize(renderer, "img/NXOR.bmp");
	NOTGate::initialize(renderer, "img/NOT.bmp");
}


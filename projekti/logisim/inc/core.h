#include <iostream>

#define ASSERT(x, ...) { if(x==false) {std::cout << "Assertion failed: " << __VA_ARGS__; std::cout << '\n'; throw;}}
#define debug(x) std::cout << x << std::endl;


namespace core{

	struct ColorRGB{
		int r, g, b;

		ColorRGB(int r, int g, int b){
			this->r = r;
			this->g = g;
			this->b = b;
		}
		float floatR() const {return float(this->r)/255.0f;}
		float floatG() const {return float(this->g)/255.0f;}
		float floatB() const {return float(this->b)/255.0f;}
	};

	inline void initializeSDL() {
		if(SDL_Init(SDL_INIT_VIDEO) < 0){
       		std::cout << "SDL could not be initialized: " << SDL_GetError();
    	}
    	else{
    		std::cout << "SDL video system is ready to go\n";
    	}
    	
    	SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 4);
    	SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 1);
	    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE);
	
    	SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER,1);
    	SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE,24);

    	//IMG_Init(IMG_INIT_PNG);
		//int imgInitResult = IMG_Init(imgFlags);
		//if (!(imgInitResult & 1)){
		//	std::cout << "Failed to initialize SDL2_image." << SDL_GetError();
		//}
	}

	bool inRect(int mouseX, int mouseY, int x, int y, int w, int h){
		return (mouseX >= x && mouseX <= x+w && mouseY >= y && mouseY <= y+h);
	}
}
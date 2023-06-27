#include <bits/stdc++.h>

#include <SDL2/SDL.h>
#include <glad/glad.h>
#include "core.h"
#include "Gate.h"
#include "Input.h"
//#include "Edge.h"

const int MAX_G = 1e4+3;
const int windowWidth = 1600;
const int windowHeight = 900;

core::ColorRGB bgColor(194, 238, 242);
core::ColorRGB nodeColor(74, 141, 247);
core::ColorRGB nodeSelected(44, 209, 118);

extern std::vector<Gate*> Gate::objects;
extern std::vector<Input*> Input::inputs;
int mouseX=0, mouseY=0;
int px=0, py=0;
bool mouseDown = false;
int movingID = -1, movingButtonID = -1;

int leftNode = 0, rightNode = 0, which = -1;
std::set<std::pair<int, int>> graph[MAX_G];
bool ok;
struct Edge{
    int a, b;
    int x1, y1;
    int x2, y2;
    int which;
    bool state = false;

    Edge(int a, int b, int x1, int y1, int x2, int y2, int which){
        this->a = a;
        this->b = b;
        this->x1 = x1;
        this->x2 = x2;
        this->y1 = y1;
        this->y2 = y2;
        this->which = which;
    }
    void render(SDL_Renderer* renderer){
        auto lGate = Gate::getObjects()[a];
        auto rGate = Gate::getObjects()[b];
        if(!ok) {std::cout << "uso sam " << lGate->id << " " << rGate->id << std::endl; ok=1;}
        if(which==0){
            //edge = std::make_unique<Edge>(leftNode, rightNode, lGate->getX(), lGate->getY()+16,
            //rGate->getX(), rGate->getY()+32);
            x1 = lGate->getX();
            y1 = lGate->getY()+16;
            x2 = rGate->getX()+128;
            y2 = rGate->getY()+32;
        }
        if(which==1){
            //edge = std::make_unique<Edge>(leftNode, rightNode, lGate->getX(), lGate->getY()+48,
            //rGate->getX(), rGate->getY()+32);
            x1 = lGate->getX();
            y1 = lGate->getY()+48;
            x2 = rGate->getX()+128;
            y2 = rGate->getY()+32;
        }
        SDL_RenderDrawLine(renderer, x1, y1, x2, y2);
        SDL_RenderDrawLine(renderer, x1, y1-1, x2, y2-1);
        SDL_RenderDrawLine(renderer, x1, y1+1, x2, y2+1);
        SDL_RenderDrawLine(renderer, x1-1, y1, x2-1, y2);
        SDL_RenderDrawLine(renderer, x1+1, y1, x2+1, y2);
        SDL_RenderDrawLine(renderer, x1-1, y1+1, x2-1, y2+1);
        SDL_RenderDrawLine(renderer, x1+1, y1-1, x2+1, y2-1);
    }


    bool operator<(const Edge& other) const {
        // Define your comparison logic here
        // For example, compare based on the 'a' member variable
        return a < other.a;
    }

};
std::set<Edge> edgeList;

int main(int argc, char* argv[]){

    SDL_Window* window=nullptr;
    core::initializeSDL();

    window = SDL_CreateWindow("Logisim v2", (1920-windowWidth)/2, (1080-windowHeight)/3, windowWidth, windowHeight,
            SDL_WINDOW_SHOWN | SDL_WINDOW_OPENGL);
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    SDL_GLContext context;
    context = SDL_GL_CreateContext(window);

    gladLoadGLLoader(SDL_GL_GetProcAddress);
    SDL_Event event;
    bool isRunning = true;
    glViewport(0, 0, windowWidth, windowHeight);

    initializeGates(renderer);
    //initializeIO(renderer);
    SDL_Surface* img1 = SDL_LoadBMP("img/ButtonPressed.bmp");
    SDL_Texture* pressed = SDL_CreateTextureFromSurface(renderer, img1);
    SDL_Surface* img2 = SDL_LoadBMP("img/ButtonReleased.bmp");
    SDL_Texture* released = SDL_CreateTextureFromSurface(renderer, img2);

    ANDGate a(60, 30);
    NANDGate b(400, 30);
    ORGate c(200, 20);
    Input button(600, 600, 0);
    NORGate d(70, 150);
    XORGate e(190, 140);
    NXORGate f(420, 160);
    NXORGate e0(600, 400);
    //NXORGate e1(800, 400);
    

    std::cout << Gate::getObjects().size() << std::endl;
    for(auto x : Gate::getObjects()){
        std::cout << x->id << std::endl;
    }


    while(isRunning){
        px = mouseX; py = mouseY;
        SDL_GetMouseState(&mouseX, &mouseY);       

        while(SDL_PollEvent(&event)){
            if(event.type == SDL_QUIT){
                isRunning = false;
            }
            if(event.type == SDL_MOUSEBUTTONUP) {
                mouseDown = false;
                movingID = -1;
                movingButtonID = -1;

                auto inp = Input::getInputs();
                for(int i=0; i<inp.size(); i+=2){
                    if(core::inRect(mouseX, mouseY, inp[i]->getX(),
                      inp[i]->getY(), inp[i]->getSize(), inp[i]->getSize())){
                        inp[i]->state ^= 1;
                        break;
                    }
                }
                auto objs = Gate::getObjects();
                for(int i=0; i<objs.size(); i+=2){
                    if(objs[i]->getInA().isInArea(mouseX, mouseY)){
                        std::cout << "GRMILICA" << std::endl;
                        leftNode = objs[i]->id;
                        which = 0;
                    }
                    if(objs[i]->getInB().isInArea(mouseX, mouseY)){
                        std::cout << "TEBRASTI" << std::endl;
                        leftNode = objs[i]->id;
                        which = 1;
                    }
                    if(objs[i]->getOutputNode().isInArea(mouseX, mouseY)){
                        std::cout << "RESILICA" << std::endl;
                        rightNode = objs[i]->id;
                        
                    }
                }
            }
            if(event.type == SDL_MOUSEBUTTONDOWN){
                mouseDown = true;
                
                auto inp = Input::getInputs();
                for(int i=0; i<inp.size(); i+=2){
                    if(core::inRect(mouseX, mouseY, inp[i]->getX(),
                      inp[i]->getY(), inp[i]->getSize(), inp[i]->getSize())){
                        movingButtonID = inp[i]->id;
                        break;
                    }
                }
                auto objs = Gate::getObjects();
                for(int i=0; i<objs.size(); i+=2){
                    if(core::inRect(mouseX, mouseY, objs[i]->getX(),
                      objs[i]->getY(), objs[i]->getW(), objs[i]->getH())){
                        movingID = objs[i]->id;
                        break;
                    }
                }
                std::cout << mouseX << ", " << mouseY << std::endl;
            }
            if(event.type == SDL_KEYUP){
                const Uint8* state = SDL_GetKeyboardState(NULL);
                if(state[SDL_SCANCODE_A]){
                    ANDGate a(mouseX, mouseY);
                }
                if(state[SDL_SCANCODE_X]){
                    XORGate x(mouseX, mouseY);
                }
                if(state[SDL_SCANCODE_O]){
                    ORGate o(mouseX, mouseY);
                }
            }
            /*
            if(event.type == SDL_KEYUP){
                if(event.key.keysym.sym == SDLK_a){
                    ANDGate a(mouseX, mouseY);
                }
                if(event.key.keysym.sym == SDLK_x){
                    XORGate x(mouseX, mouseY);
                }
                if(event.key.keysym.sym == SDLK_o){
                    ORGate o(mouseX, mouseY);
                }
            }
            */
        }

        if(leftNode>0 && rightNode>0){
            bool exist = false;
            for(auto x : graph[rightNode]){
                if(x.first==leftNode && x.second == which) {
                    exist = true;
                    //std::cout << "jbg" << std::endl;
                    graph[leftNode].erase(std::make_pair(rightNode, which));
                    graph[rightNode].erase(std::make_pair(leftNode, which));
                    for(auto edge : edgeList){
                        if((edge.a==leftNode && edge.b==rightNode) || (edge.a==rightNode && edge.b==leftNode)){
                            edgeList.erase(edge);
                            break;
                        }
                    }
                    break;
                    //SDL_SetRenderDrawColor(renderer, bgColor.r, bgColor.g, bgColor.b, 255);
                    //SDL_RenderDrawLine(renderer, Gate::objects[leftNode]->getX(), Gate::objects[leftNode]->getY(),
                    //    Gate::objects[rightNode]->getX(), Gate::objects[rightNode]->getY());
                }
            }
            if(!exist){
                    //std::cout << "reeeesi" << leftNode << " " << rightNode << std::endl;
                    graph[leftNode].insert({rightNode, which});
                    graph[rightNode].insert({leftNode, which});
                    //std::unique_ptr<Edge> edge;
                    auto lGate = Gate::getObjects()[leftNode];
                    auto rGate = Gate::getObjects()[rightNode];
                    if(which==0){
                        //edge = std::make_unique<Edge>(leftNode, rightNode, lGate->getX(), lGate->getY()+16,
                        //rGate->getX(), rGate->getY()+32);
                        //std::cout << "fef" << std::endl;
                        Edge edge(leftNode, rightNode, lGate->getX(), lGate->getY()+16,
                          rGate->getX()+128, rGate->getY()+32, 0);
                        edgeList.insert(edge);
                    }
                    if(which==1){
                        //std::cout << "fefe" << std::endl;
                        //edge = std::make_unique<Edge>(leftNode, rightNode, lGate->getX(), lGate->getY()+48,
                        //rGate->getX(), rGate->getY()+32);
                        Edge edge(leftNode, rightNode, lGate->getX(), lGate->getY()+48,
                          rGate->getX()+128, rGate->getY()+32, 1);
                        edgeList.insert(edge);
                        ok=0;

                    }
                    //edgeList.emplace(edge.get());

            }
            leftNode = 0;
            rightNode = 0; 
            which = -1;  
        }

        if(mouseDown){
            if(movingButtonID>-1){
                auto inpjut = Input::getInputs()[movingButtonID];
                if(core::inRect(mouseX, mouseY, inpjut->getX(),
                  inpjut->getY(), inpjut->getSize(), inpjut->getSize())){
                    inpjut->addXY(mouseX-px, mouseY-py);
                }

            }
            else if(movingID>-1){
                auto movingObj = Gate::getObjects()[movingID];
                if(core::inRect(mouseX, mouseY, movingObj->getX(),
                  movingObj->getY(), movingObj->getW(), movingObj->getH())){
                    movingObj->addXY(mouseX-px, mouseY-py);
                }
                //if(objects[i].second==0)
                //if(objects[i].second==1) 
                //if(objects[i].second==2) 
                //if(objects[i].second==3) 
                //if(objects[i].second==4) 
                //if(objects[i].second==5) a5=
            }
        }

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        for(auto edge : edgeList){
            edge.render(renderer);
        }

        auto in = Input::getInputs();
        for(int i=0; i<in.size(); i+=2){
            SDL_Rect rect = {in[i]->getX(), in[i]->getY(), in[i]->getSize(), in[i]->getSize()};
            if(in[i]->state==true) SDL_RenderCopy(renderer, pressed, NULL, &rect);
            else SDL_RenderCopy(renderer, released, NULL, &rect);
            Input::getInputs()[i]->render(renderer, nodeColor.r, nodeColor.g, nodeColor.b);
        }
        for(int i=0; i<Gate::getObjects().size(); i+=2){
            Gate::getObjects()[i]->render(renderer, nodeColor.r, nodeColor.g, nodeColor.b);
        }
        if(leftNode>0){
            //std::cout << "--->l " << leftNode << std::endl;
            Gate::getObjects()[leftNode]->postRender(renderer, which, nodeSelected.r, nodeSelected.g, nodeSelected.b);
        }
        if(rightNode>0){
            //std::cout << "--->r " << rightNode << std::endl;
            Gate::getObjects()[rightNode]->postRender(renderer, 2, nodeSelected.r, nodeSelected.g, nodeSelected.b);
        }
        // Update the //screen
        SDL_RenderPresent(renderer);

        glClearColor(bgColor.floatR(), bgColor.floatG(), bgColor.floatB(), 1.0f);
        //glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT);

        SDL_GL_SwapWindow(window);
    }
    SDL_DestroyWindow(window);
    
    SDL_Delay(800);
    //IMG_Quit();
    SDL_Quit();
    return 0;
}

#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

using namespace cv;

int main(int , char **)
{
    VideoCapture cap(0);
    while(!cap.isOpened()) return -1;

    Mat frame, edges;
    namedWindow("edges",1);
    for(;;)
    {
        cap >>frame;
        cvtColor(frame,edges,COLOR_BGR2GRAY);
        GaussianBlur(edges,edges,Size(7,7),1.5,1.5);
        imshow("edges",edges);
        if(waitKey(30) >= 0) break;
    }
    return 0;
}
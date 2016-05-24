// AntiVC_Demo.cpp : AntiVC.dll演示程序。
//

#include<stdio.h>
#include <iostream>
#include <Windows.h>
int main(int argc, char *argv[])
{
	if (argc < 2)
		return -1;
	char imgstr[40];
	strcpy(imgstr, argv[1]);
	HINSTANCE hInst = LoadLibraryA("AntiVC.dll");//载入AntiVC.dll
	if (!hInst)
	{
		std::cout<<"无法加载 AntiVC.Dll!";
		getchar();
		return 0;
	}

/*
	AntiVC.dll导出函数说明：
	int LoadCdsFromBuffer(//成功返回当前识别库文件索引，失败返回-1
	char[] FileBuffer, //识别库文件二进制数据
	int FileBufLen,//识别库文件数据尺寸
	char[] Password);//识别库调用密码

	int LoadCdsFromFile(//成功返回当前识别库文件索引，失败返回-1
	char[] FilePath，//识别库文件所在路径
	char[] Password);//识别库文件所在路径

	-------以上两个函数用于载入识别库文件----------

	bool GetVcodeFromBuffer(  //能识别返回真，否则返回假
	int CdsFileIndex ,//识别库文件索引
	char* ImgBuffer , //验证码图像二进制数据
	int ImgBufLen ,//验证码图像尺寸
	char[] Vcode);//返回的已识别验证码文本

	bool GetVcodeFromFile( //能识别返回真，否则返回假
	int CdsFileIndex ,//识别库文件索引
	char[] FilePath , //验证码文件所在路径
	char[] Vcode);   //返回的已识别验证码文本

	-------以上两个函数用于识别验证码----------

*/	
	//-----------LoadCdsFromFile------------
	typedef int (CALLBACK* LPLoadCds)(char[],char[]);
	LPLoadCds LoadCdsFromFile = (LPLoadCds)GetProcAddress(hInst, "LoadCdsFromFile");

/*
	//-----------LoadCdsFromBuffer------------
	typedef int (CALLBACK* LPLoadCds)(char[],int,char[]);
	LPLoadCds LoadCdsFromBuffer = (LPLoadCds)GetProcAddress(hInst, "LoadCdsFromBuffer");
*/

	int index = LoadCdsFromFile ("B196.pdb","AvXv5d5,mb5fx4");//载入识别库

	if (index == -1)//返回-1说明载入识别库出错
	{
		std::cout<<"-1";
		getchar();
		return 0;
	}

	
	//-----------GetVcodeFromFile------------
	//typedef bool (CALLBACK* LPGetVcode)(int,char[],char[]);
	//LPGetVcode GetVcodeFromFile = (LPGetVcode)GetProcAddress(hInst, "GetVcodeFromFile");

	//-----------GetVcodeFromBuffer------------
	typedef bool (CALLBACK* LPGetVcode)(int,char*,int,char[]);
	LPGetVcode GetVcodeFromBuffer = (LPGetVcode)GetProcAddress(hInst, "GetVcodeFromBuffer");
	//for (int i = 0; i < 1; i++)
	{

	char result[7];//定义一个字符串以接收验证码，这里验证码字符数是4，所以取5.

	HANDLE pfile = CreateFile(imgstr, GENERIC_READ, FILE_SHARE_READ, 0, OPEN_EXISTING, 0, 0);

	if(pfile == INVALID_HANDLE_VALUE){
		std::cout<<"-1";
		CloseHandle(pfile);
		return 0;
	}

	unsigned long filesize = GetFileSize (pfile, NULL);
	char* buffer = new char[filesize]; 
	unsigned long readsize;
	ReadFile(pfile,buffer,filesize,&readsize,NULL);
	CloseHandle(pfile);
	
		if (GetVcodeFromBuffer(index, buffer, filesize, result))
			std::cout << result;
		else
			std::cout << "-1";
		delete buffer;
	}

//	getchar();
	return 0;
}


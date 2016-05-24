// AntiVC_Demo.cpp : AntiVC.dll��ʾ����
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
	HINSTANCE hInst = LoadLibraryA("AntiVC.dll");//����AntiVC.dll
	if (!hInst)
	{
		std::cout<<"�޷����� AntiVC.Dll!";
		getchar();
		return 0;
	}

/*
	AntiVC.dll��������˵����
	int LoadCdsFromBuffer(//�ɹ����ص�ǰʶ����ļ�������ʧ�ܷ���-1
	char[] FileBuffer, //ʶ����ļ�����������
	int FileBufLen,//ʶ����ļ����ݳߴ�
	char[] Password);//ʶ����������

	int LoadCdsFromFile(//�ɹ����ص�ǰʶ����ļ�������ʧ�ܷ���-1
	char[] FilePath��//ʶ����ļ�����·��
	char[] Password);//ʶ����ļ�����·��

	-------��������������������ʶ����ļ�----------

	bool GetVcodeFromBuffer(  //��ʶ�𷵻��棬���򷵻ؼ�
	int CdsFileIndex ,//ʶ����ļ�����
	char* ImgBuffer , //��֤��ͼ�����������
	int ImgBufLen ,//��֤��ͼ��ߴ�
	char[] Vcode);//���ص���ʶ����֤���ı�

	bool GetVcodeFromFile( //��ʶ�𷵻��棬���򷵻ؼ�
	int CdsFileIndex ,//ʶ����ļ�����
	char[] FilePath , //��֤���ļ�����·��
	char[] Vcode);   //���ص���ʶ����֤���ı�

	-------����������������ʶ����֤��----------

*/	
	//-----------LoadCdsFromFile------------
	typedef int (CALLBACK* LPLoadCds)(char[],char[]);
	LPLoadCds LoadCdsFromFile = (LPLoadCds)GetProcAddress(hInst, "LoadCdsFromFile");

/*
	//-----------LoadCdsFromBuffer------------
	typedef int (CALLBACK* LPLoadCds)(char[],int,char[]);
	LPLoadCds LoadCdsFromBuffer = (LPLoadCds)GetProcAddress(hInst, "LoadCdsFromBuffer");
*/

	int index = LoadCdsFromFile ("B196.pdb","AvXv5d5,mb5fx4");//����ʶ���

	if (index == -1)//����-1˵������ʶ������
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

	char result[7];//����һ���ַ����Խ�����֤�룬������֤���ַ�����4������ȡ5.

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


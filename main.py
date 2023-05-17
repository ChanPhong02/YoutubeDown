import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtCore import *
import pytube
import os
import re
import subprocess
from ui.Design2 import Ui_MainWindow

class YoutubeDownloader(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Youtube Downloader v2.0')


        if getattr(sys, 'frozen', False):
            # Đang chạy từ tệp exe đã đóng gói
            image_path = os.path.join(sys._MEIPASS, "youtube.png")
        else:
            # Đang chạy từ mã nguồn .py
            image_path = "resource/youtube.png"
        
        self.label_4.setPixmap(QtGui.QPixmap(image_path))

        self.resolutionComboBox.addItem('144p')
        self.resolutionComboBox.addItem('240p')
        self.resolutionComboBox.addItem('360p')
        self.resolutionComboBox.addItem('480p')
        self.resolutionComboBox.addItem('720p')

        self.comboBox.addItem('mp3')
        self.comboBox.addItem('avi')
        self.comboBox.addItem('mov')
        self.comboBox.addItem('wmv')

        self.extension.addItem('mp3')
        self.extension.addItem('avi')
        self.extension.addItem('mov')
        self.extension.addItem('wmv')
        self.extension.addItem('wav')

        self.initSignal()

        self.statusbar.showMessage('Sẵn sàng.')
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)
        self.statusbar.addPermanentWidget(self.progress_bar)

    # signal initialization
    def initSignal(self) :
        self.downloadButton.clicked.connect(self.downloadWork)
        self.toolButton.clicked.connect(self.savePathWork)
        self.fileToolButton.clicked.connect(self.selectFileWork)
        self.toolButton_2.clicked.connect(self.selectPathWork)
        self.convertButton.clicked.connect(self.convertWork)
        self.tabWidget.currentChanged.connect(self.tabClicked)

    # when the toolbox is clicked
    @pyqtSlot()
    def savePathWork(self) :
        fpath = QFileDialog.getExistingDirectory(self, 'Chọn đường dẫn')
        self.saveTextEdit.setText(fpath)

    # when the download button is clicked
    @pyqtSlot()
    def downloadWork(self) :
        # Step #1. Check url address
        url = self.urlTextEdit.text().strip()
        save = self.saveTextEdit.text()
        regex = re.compile('^https://www.youtube.com/watch?')
        regexshort = re.compile('^https://www.youtube.com/shorts/')

        if url is None or url == '' or not url :
            QMessageBox.about(self, 'Lỗi', 'Chưa nhập URL của video')
            self.urlTextEdit.setFocus(True)
            return None

        if save is None or save == '' or not save :
            QMessageBox.about(self, 'Lỗi', 'Chưa chọn đường dẫn')
            return None

        # Step #2. download progress
        if (regex.match(url) or regexshort.match(url)) is not None :
            # download video first
            self.statusbar.showMessage('Đang tải xuống...')
            x = 5
            self.progress_bar.setValue(x)
            selected_resolution = self.resolutionComboBox.currentText()

            video = pytube.YouTube(url)
            stream = video.streams.all()
            down_dir = self.saveTextEdit.text()
            selected_stream = None
            for stream in stream:
                x = x + 5
                self.progress_bar.setValue(x)
                if stream.resolution == selected_resolution and stream.includes_audio_track:
                    self.progress_bar.setValue(40)
                    selected_stream = stream
                    break

            if selected_stream is not None:
                self.progress_bar.setValue(60)
                selected_stream.download(down_dir)
                
            else:
                QMessageBox.about(self, 'Lỗi', 'Không tìm thấy độ phân giải được chọn')
                self.statusbar.showMessage('Tải xuống thất bại')  
                

            # Step #3. Check checkbox value
            if self.checkBox.isChecked() :
                self.progress_bar.setValue(80)
                oriFileName = selected_stream.default_filename
                newFileName = os.path.splitext(oriFileName)[0]

                # print(str(self.comboBox.currentText()))
                subprocess.call(['C:/ffmpeg/ffmpeg.exe','-i',
                    os.path.join(down_dir, oriFileName),
                    os.path.join(down_dir, newFileName + '.' + str(self.comboBox.currentText())), 
                ])
                self.statusbar.showMessage('Tải xuống và chuyển đổi thành công') 
                self.progress_bar.setValue(100)
            else: 
                self.statusbar.showMessage('Tải xuống thành công')
                self.progress_bar.setValue(100)
        else :
            QMessageBox.about(self,'Lỗi', 'Sai định dạng URL Youtube')

    # tabWidget when pressed
    @pyqtSlot()
    def tabClicked(self) :
        self.statusbar.showMessage('Sẵn sàng.')

    # Convert file when pressed
    @pyqtSlot()
    def selectFileWork(self) :
        self.fname = QFileDialog.getOpenFileName(self, 'Chọn video cần đổi định dạng')
        self.fileTextEdit.setText(self.fname[0])

    # Convert toolbutton when pressed
    @pyqtSlot()
    def selectPathWork(self) :
        fpath = QFileDialog.getExistingDirectory(self, 'Chọn đường dẫn để lưu video')
        self.savePathEdit.setText(fpath)

    # Convert file logic
    @pyqtSlot()
    def convertWork(self) :
        file_dir = self.fileTextEdit.text()
        down_dir = self.savePathEdit.text()

        if file_dir is None or file_dir == '' or not file_dir :
            QMessageBox.about(self, 'Lỗi', 'Chưa chọn tệp')
            return None

        if down_dir is None or down_dir == '' or not down_dir :
            QMessageBox.about(self, 'Lỗi', 'Chưa chọn đường dẫn')
            return None
        x = 50
        self.progress_bar.setValue(x)

        fileName = os.path.basename(file_dir)
        newFileName = os.path.splitext(fileName)[0]

        subprocess.call(['C:/ffmpeg/ffmpeg.exe','-i',
            os.path.join(file_dir),
            os.path.join(down_dir, newFileName + '.' + str(self.extension.currentText()))
        ])
        self.progress_bar.setValue(100)
        self.statusbar.showMessage('Chuyển đổi hoàn tất')

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    you_viewer_main = YoutubeDownloader()
    you_viewer_main.show()
    app.exec_()

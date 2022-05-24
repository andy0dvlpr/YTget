namespace YTget
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.audioRadio = new System.Windows.Forms.RadioButton();
            this.downloadTypeGroupBox = new System.Windows.Forms.GroupBox();
            this.videoPLCheckBox = new System.Windows.Forms.CheckBox();
            this.videoRadio = new System.Windows.Forms.RadioButton();
            this.audioPLCheckBox = new System.Windows.Forms.CheckBox();
            this.bitrateLabel = new System.Windows.Forms.Label();
            this.downloadSettingsGroupBox = new System.Windows.Forms.GroupBox();
            this.fileNameLabel = new System.Windows.Forms.Label();
            this.saveLocationBox = new System.Windows.Forms.TextBox();
            this.saveLocationLabel = new System.Windows.Forms.Label();
            this.fileNameFormatLink = new System.Windows.Forms.LinkLabel();
            this.fileNameBox = new System.Windows.Forms.TextBox();
            this.bitrateBox = new System.Windows.Forms.TextBox();
            this.ytURLLabel = new System.Windows.Forms.Label();
            this.ytURLBox = new System.Windows.Forms.TextBox();
            this.downloadButton = new System.Windows.Forms.Button();
            this.downloadTypeGroupBox.SuspendLayout();
            this.downloadSettingsGroupBox.SuspendLayout();
            this.SuspendLayout();
            // 
            // audioRadio
            // 
            this.audioRadio.AutoSize = true;
            this.audioRadio.Checked = true;
            this.audioRadio.Location = new System.Drawing.Point(6, 22);
            this.audioRadio.Name = "audioRadio";
            this.audioRadio.Size = new System.Drawing.Size(57, 19);
            this.audioRadio.TabIndex = 0;
            this.audioRadio.TabStop = true;
            this.audioRadio.Text = "Audio";
            this.audioRadio.UseVisualStyleBackColor = true;
            // 
            // downloadTypeGroupBox
            // 
            this.downloadTypeGroupBox.Controls.Add(this.videoPLCheckBox);
            this.downloadTypeGroupBox.Controls.Add(this.videoRadio);
            this.downloadTypeGroupBox.Controls.Add(this.audioPLCheckBox);
            this.downloadTypeGroupBox.Controls.Add(this.audioRadio);
            this.downloadTypeGroupBox.Location = new System.Drawing.Point(12, 12);
            this.downloadTypeGroupBox.Name = "downloadTypeGroupBox";
            this.downloadTypeGroupBox.Size = new System.Drawing.Size(200, 127);
            this.downloadTypeGroupBox.TabIndex = 1;
            this.downloadTypeGroupBox.TabStop = false;
            this.downloadTypeGroupBox.Text = "Download type";
            // 
            // videoPLCheckBox
            // 
            this.videoPLCheckBox.AutoSize = true;
            this.videoPLCheckBox.Location = new System.Drawing.Point(26, 97);
            this.videoPLCheckBox.Name = "videoPLCheckBox";
            this.videoPLCheckBox.Size = new System.Drawing.Size(63, 19);
            this.videoPLCheckBox.TabIndex = 3;
            this.videoPLCheckBox.Text = "Playlist";
            this.videoPLCheckBox.UseVisualStyleBackColor = true;
            // 
            // videoRadio
            // 
            this.videoRadio.AutoSize = true;
            this.videoRadio.Location = new System.Drawing.Point(6, 72);
            this.videoRadio.Name = "videoRadio";
            this.videoRadio.Size = new System.Drawing.Size(55, 19);
            this.videoRadio.TabIndex = 2;
            this.videoRadio.Text = "Video";
            this.videoRadio.UseVisualStyleBackColor = true;
            // 
            // audioPLCheckBox
            // 
            this.audioPLCheckBox.AutoSize = true;
            this.audioPLCheckBox.Location = new System.Drawing.Point(26, 47);
            this.audioPLCheckBox.Name = "audioPLCheckBox";
            this.audioPLCheckBox.Size = new System.Drawing.Size(63, 19);
            this.audioPLCheckBox.TabIndex = 1;
            this.audioPLCheckBox.Text = "Playlist";
            this.audioPLCheckBox.UseVisualStyleBackColor = true;
            // 
            // bitrateLabel
            // 
            this.bitrateLabel.AutoSize = true;
            this.bitrateLabel.Location = new System.Drawing.Point(6, 26);
            this.bitrateLabel.Name = "bitrateLabel";
            this.bitrateLabel.Size = new System.Drawing.Size(41, 15);
            this.bitrateLabel.TabIndex = 2;
            this.bitrateLabel.Text = "Bitrate";
            // 
            // downloadSettingsGroupBox
            // 
            this.downloadSettingsGroupBox.Controls.Add(this.fileNameLabel);
            this.downloadSettingsGroupBox.Controls.Add(this.saveLocationBox);
            this.downloadSettingsGroupBox.Controls.Add(this.saveLocationLabel);
            this.downloadSettingsGroupBox.Controls.Add(this.fileNameFormatLink);
            this.downloadSettingsGroupBox.Controls.Add(this.fileNameBox);
            this.downloadSettingsGroupBox.Controls.Add(this.bitrateBox);
            this.downloadSettingsGroupBox.Controls.Add(this.bitrateLabel);
            this.downloadSettingsGroupBox.Location = new System.Drawing.Point(218, 12);
            this.downloadSettingsGroupBox.Name = "downloadSettingsGroupBox";
            this.downloadSettingsGroupBox.Size = new System.Drawing.Size(492, 127);
            this.downloadSettingsGroupBox.TabIndex = 3;
            this.downloadSettingsGroupBox.TabStop = false;
            this.downloadSettingsGroupBox.Text = "Download settings";
            // 
            // fileNameLabel
            // 
            this.fileNameLabel.AutoSize = true;
            this.fileNameLabel.Location = new System.Drawing.Point(6, 60);
            this.fileNameLabel.Name = "fileNameLabel";
            this.fileNameLabel.Size = new System.Drawing.Size(58, 15);
            this.fileNameLabel.TabIndex = 10;
            this.fileNameLabel.Text = "File name";
            // 
            // saveLocationBox
            // 
            this.saveLocationBox.Location = new System.Drawing.Point(89, 94);
            this.saveLocationBox.Name = "saveLocationBox";
            this.saveLocationBox.Size = new System.Drawing.Size(307, 23);
            this.saveLocationBox.TabIndex = 9;
            this.saveLocationBox.Text = "%userprofile%\\Downloads";
            // 
            // saveLocationLabel
            // 
            this.saveLocationLabel.AutoSize = true;
            this.saveLocationLabel.Location = new System.Drawing.Point(6, 97);
            this.saveLocationLabel.Name = "saveLocationLabel";
            this.saveLocationLabel.Size = new System.Drawing.Size(77, 15);
            this.saveLocationLabel.TabIndex = 8;
            this.saveLocationLabel.Text = "Save location";
            // 
            // fileNameFormatLink
            // 
            this.fileNameFormatLink.AutoSize = true;
            this.fileNameFormatLink.Font = new System.Drawing.Font("Segoe UI", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.fileNameFormatLink.Location = new System.Drawing.Point(92, 78);
            this.fileNameFormatLink.Name = "fileNameFormatLink";
            this.fileNameFormatLink.Size = new System.Drawing.Size(302, 13);
            this.fileNameFormatLink.TabIndex = 7;
            this.fileNameFormatLink.TabStop = true;
            this.fileNameFormatLink.Text = "https://github.com/ytdl-org/youtube-dl#output-template";
            this.fileNameFormatLink.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLabel1_LinkClicked);
            // 
            // fileNameBox
            // 
            this.fileNameBox.Location = new System.Drawing.Point(89, 52);
            this.fileNameBox.Name = "fileNameBox";
            this.fileNameBox.Size = new System.Drawing.Size(307, 23);
            this.fileNameBox.TabIndex = 5;
            this.fileNameBox.Text = "%(title)";
            // 
            // bitrateBox
            // 
            this.bitrateBox.Location = new System.Drawing.Point(89, 23);
            this.bitrateBox.Name = "bitrateBox";
            this.bitrateBox.Size = new System.Drawing.Size(70, 23);
            this.bitrateBox.TabIndex = 3;
            this.bitrateBox.Text = "192";
            // 
            // ytURLLabel
            // 
            this.ytURLLabel.AutoSize = true;
            this.ytURLLabel.Location = new System.Drawing.Point(18, 142);
            this.ytURLLabel.Name = "ytURLLabel";
            this.ytURLLabel.Size = new System.Drawing.Size(29, 15);
            this.ytURLLabel.TabIndex = 4;
            this.ytURLLabel.Text = "Link";
            // 
            // ytURLBox
            // 
            this.ytURLBox.Location = new System.Drawing.Point(18, 160);
            this.ytURLBox.Name = "ytURLBox";
            this.ytURLBox.Size = new System.Drawing.Size(682, 23);
            this.ytURLBox.TabIndex = 5;
            // 
            // downloadButton
            // 
            this.downloadButton.Location = new System.Drawing.Point(321, 189);
            this.downloadButton.Name = "downloadButton";
            this.downloadButton.Size = new System.Drawing.Size(75, 23);
            this.downloadButton.TabIndex = 6;
            this.downloadButton.Text = "Download";
            this.downloadButton.UseVisualStyleBackColor = true;
            this.downloadButton.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(712, 216);
            this.Controls.Add(this.downloadButton);
            this.Controls.Add(this.ytURLBox);
            this.Controls.Add(this.ytURLLabel);
            this.Controls.Add(this.downloadSettingsGroupBox);
            this.Controls.Add(this.downloadTypeGroupBox);
            this.Name = "Form1";
            this.Text = "YTget";
            this.downloadTypeGroupBox.ResumeLayout(false);
            this.downloadTypeGroupBox.PerformLayout();
            this.downloadSettingsGroupBox.ResumeLayout(false);
            this.downloadSettingsGroupBox.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private RadioButton audioRadio;
        private GroupBox downloadTypeGroupBox;
        private CheckBox videoPLCheckBox;
        private RadioButton videoRadio;
        private CheckBox audioPLCheckBox;
        private Label bitrateLabel;
        private GroupBox downloadSettingsGroupBox;
        private TextBox fileNameBox;
        private TextBox bitrateBox;
        private LinkLabel fileNameFormatLink;
        private TextBox saveLocationBox;
        private Label saveLocationLabel;
        private Label ytURLLabel;
        private TextBox ytURLBox;
        private Button downloadButton;
        private Label fileNameLabel;
    }
}
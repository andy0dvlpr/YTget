using System.Diagnostics;

namespace YTget
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //https://brockallen.com/2016/09/24/process-start-for-urls-on-net-core/
        private void OpenUrl(string url)
        {
            try
            {
                Process.Start(url);
            }
            catch
            {
                // hack because of this: https://github.com/dotnet/corefx/issues/10361
                url = url.Replace("&", "^&");
                Process.Start(new ProcessStartInfo(url) { UseShellExecute = true });
            }
        }

        //https://stackoverflow.com/a/1469790
        private void RunCMD(string cmd)
        {
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = "/C " + cmd;
            process.StartInfo = startInfo;
            process.Start();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            this.fileNameFormatLink.LinkVisited = true; // Change link color to show it's been visited.
            OpenUrl("https://github.com/ytdl-org/youtube-dl#output-template");
        }
        private void audioIcon_Click(object sender, EventArgs e)
        {
            audioRadio.Checked = true;
        }

        private void videoIcon_Click(object sender, EventArgs e)
        {
            videoRadio.Checked = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Stupid but it works. I'm not bothering with LINQ or whatever.
            bool audiochecked = audioRadio.Checked;
            bool playlistchecked = playlistCheckBox.Checked;
            bool videochecked = videoRadio.Checked;
            int bitrate = int.Parse(bitrateBox.Text);
            string fileName = fileNameBox.Text;
            string saveLocation = saveLocationBox.Text;
            string ytURL = ytURLBox.Text;

            // I feel like YandereDev. Suggestions are welcome.
            if (audiochecked)
            {
                if (!playlistchecked)
                {
                    RunCMD($"youtube-dl.exe -x --audio-format mp3 --audio-quality {bitrate}k -o \"{saveLocation}\\{fileName}.%(ext)s\" \"{ytURL}\"");

                }
                if (playlistchecked)
                {
                    RunCMD($"youtube-dl.exe --yes-playlist -x --audio-format mp3 --audio-quality {bitrate}k -o \"{saveLocation}\\{fileName}.%(ext)s\" \"{ytURL}\"");
                }
            }
            if (videochecked)
            {
                if (!playlistchecked)
                {
                    RunCMD($"youtube-dl.exe -f mp4 -o \"{saveLocation}\\{fileName}.%(ext)s\" \"{ytURL}\"");
                }
                if (playlistchecked)
                {
                    RunCMD($"youtube-dl.exe --yes-playlist -f mp4 -o \"{saveLocation}\\{fileName}.%(ext)s\" \"{ytURL}\"");
                }
            }
        }
    }
}
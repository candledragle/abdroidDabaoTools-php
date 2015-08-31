使用步骤：
1、使用支持在代码中读取渠道号的统计平台（比如 umeng 以下已umeng为例）
2.在软件的启动Activtiy读取渠道号
  例如：
    String channel = KHelper.getChannel(getBaseContext());
    AnalyticsConfig.setChannel(channel);

 3.打包一个官方版本，然后将各个渠道号添加进脚本中，运行脚本各个渠道包就打好了，注意替换掉对用的名字

public static String getChannel(Context context) {
        ApplicationInfo appinfo = context.getApplicationInfo();
        String sourceDir = appinfo.sourceDir;

        KLog.i("sym: ", sourceDir);
        String ret = "";
        ZipFile zipfile = null;
        try {
            zipfile = new ZipFile(sourceDir);
            Enumeration<?> entries = zipfile.entries();
            while (entries.hasMoreElements()) {
                ZipEntry entry = ((ZipEntry) entries.nextElement());
                String entryName = entry.getName();
                KLog.i("sym: ", entryName);
                String[] split = entryName.split("/");
                entryName = split[split.length - 1];
                if (entryName.startsWith("tqchannel")) {

                    ret = entryName;
                    KLog.i("sym_ret", ret);
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (zipfile != null) {
                try {
                    zipfile.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        KLog.i("sym", "the channel file name is " + ret);
        String[] split = ret.split("_");
        if (split != null && split.length >= 2) {
            return ret.substring(split[0].length() + 1);

        } else {
            return "";
        }
    } 安卓多渠道打包很累，想想就是替换掉工程中项目标示。这是一个php 脚本文件，旨在减轻打包的工作

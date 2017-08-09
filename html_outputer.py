# encoding:utf-8
# 输出器


class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):       # 收集html数据
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):                  #生成html文件
        fout = open('output.html', 'w')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        # 默认ascii编码   需要转码utf-8
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()


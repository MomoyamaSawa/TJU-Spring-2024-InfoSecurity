import time
import gradio as gr
import backend

obeject_choices = ["测试"]


def generate_product(dropdown):
    _id = backend.new_product()
    product_list = backend.get_product(_id)
    product_list_display = generate_list(product_list)
    return _id, product_list_display


def show_info(adress):
    strings = backend.get_object(adress)
    return "".join(
        f"![Image]({strings[2]})<br>**厂家名称**：{strings[0]}<br>**联系方式**：{strings[1]}<br>**类别**：{strings[3]}<br>**地址**：{strings[4]}<br>**描述**：{strings[5]}<br>"
    )


def generate_list(product_list):
    return "".join(
        [
            f"**[第{idx + 1}站]**<br>**时间**：{time.strftime('%Y年%m月%d日%H时%M分', time.localtime(int(item[0])))}<br>**溯源地址**：{item[1]}<br>**审查员**：{item[2]}<br><br>**↓↓↓↓↓**<br><br>"
            for idx, item in enumerate(product_list)
        ]
    )


with gr.Blocks() as demo:

    gr.Image("./title.png", show_label=False)
    gr.Markdown("# ⭐区块链茅台酒溯源 DEMO")
    gr.Markdown(
        "2151641王佳垚，先点击随机生成产品按钮，左侧会随机生成一瓶茅台酒产品和它的生产销售路径，从生产销售路径中选择一个溯源地址可以在右侧输入，然后查询到节点厂家商家的详细信息"
    )

    with gr.Row():
        with gr.Column():
            with gr.Tab("1. 茅台酒产品溯源链"):
                gr.Markdown("## 1. 茅台酒产品溯源链")
                gr.Image("./process.png", label="茅台酒生产销售流程")
                product_label = gr.Label(
                    value="点击按钮生成一个茅台酒产品", label="茅台酒产品唯一ID"
                )
                product_list_md = gr.Markdown("在这里会显示茅台酒产品溯源链")
                product_button = gr.Button("随机生成产品", variant="primary")
                product_button.click(
                    fn=generate_product,
                    outputs=[product_label, product_list_md],
                )

        with gr.Column():
            with gr.Tab("2. 溯源信息查询"):
                gr.Markdown("## 2.溯源信息查询")
                object_input = gr.Textbox(
                    label="溯源地址", placeholder="请输入溯源地址"
                )
                object_md = gr.Markdown("在这里会显示溯源信息")
                object_button = gr.Button("查询溯源信息", variant="primary")
                object_button.click(
                    fn=show_info, inputs=object_input, outputs=object_md
                )

demo.launch()

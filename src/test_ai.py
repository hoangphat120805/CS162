import google.generativeai as genai
import google.ai.generativelanguage as glm
from process_file import outputAsJson, outputAsCSV

genai.configure(api_key="API_KEY")

func = glm.Tool(
    function_declarations=[
        glm.FunctionDeclaration(
            name='searchRoute',
            description="This function find route of bus by attributes.",
            parameters=glm.Schema(
                type=glm.Type.OBJECT,
                properties={
                    'route_id': glm.Schema(type=glm.Type.INTEGER),
                    'route_var_id': glm.Schema(type=glm.Type.INTEGER),
                    'route_var_name': glm.Schema(type=glm.Type.STRING),
                    'route_var_short_name': glm.Schema(type=glm.Type.STRING),
                    'route_no': glm.Schema(type=glm.Type.STRING),
                    'start_stop': glm.Schema(type=glm.Type.STRING),
                    'end_stop': glm.Schema(type=glm.Type.STRING),
                    'distance': glm.Schema(type=glm.Type.NUMBER),
                    'outbound': glm.Schema(type=glm.Type.BOOLEAN),
                    'running_time': glm.Schema(type=glm.Type.NUMBER),
                }
            )
        ), 
        glm.FunctionDeclaration(
            name='searchStop',
            description="This function find stop of bus by attributes",
            parameters=glm.Schema(
                type=glm.Type.OBJECT,
                properties={
                    'stop_id': glm.Schema(type=glm.Type.INTEGER),
                    'code': glm.Schema(type=glm.Type.STRING),
                    'name': glm.Schema(type=glm.Type.STRING),
                    'stop_type': glm.Schema(type=glm.Type.STRING),
                    'zone': glm.Schema(type=glm.Type.STRING),
                    'ward': glm.Schema(type=glm.Type.STRING),
                    'address_no': glm.Schema(type=glm.Type.STRING),
                    'street': glm.Schema(type=glm.Type.STRING),
                    'support_disability': glm.Schema(type=glm.Type.STRING),
                    'status': glm.Schema(type=glm.Type.STRING),
                    'lng': glm.Schema(type=glm.Type.NUMBER),
                    'lat': glm.Schema(type=glm.Type.NUMBER),
                    'search': glm.Schema(type=glm.Type.STRING),
                    'routes': glm.Schema(type=glm.Type.STRING),
                }
            )
        ),
        glm.FunctionDeclaration(
            name='searchPath',
            description="This function find path of bus by attributes",
            parameters=glm.Schema(
                type=glm.Type.OBJECT,
                properties={
                    'lat': glm.Schema(type=glm.Type.ARRAY),
                    'lng': glm.Schema(type=glm.Type.ARRAY),
                    'route_id': glm.Schema(type=glm.Type.INTEGER),
                    'route_var_id': glm.Schema(type=glm.Type.INTEGER),
                }
            )
        ),
        glm.FunctionDeclaration(
            name='shortest_path',
            description="This function find shortest path between two stops",
            parameters=glm.Schema(
                type=glm.Type.OBJECT,
                properties={
                    'start_stop': glm.Schema(type=glm.Type.INTEGER),
                    'end_stop': glm.Schema(type=glm.Type.INTEGER),
                }
            )
        ),
        
    ]
)



def test_ai(routes, stops, paths, graph):
    # model = genai.GenerativeModel(model_name='gemini-pro', tools= )
    model = genai.GenerativeModel(model_name='gemini-pro', tools=func)
    chat = model.start_chat()
    while True:
        query = input("Enter your query(enter 0 to exit): ")
        if query == '0':
            break
        response = chat.send_message(query)
        # print(response)
        fc = response.candidates[0].content.parts[0].function_call
        if fc.name == 'shortest_path':
            start_stop = fc.args['start_stop']
            start_stop = int(start_stop)
            end_stop = fc.args['end_stop']
            end_stop = int(end_stop)
            outputAsJson("src/output/output", graph.shortest_path(start_stop, end_stop))
        elif fc.name == 'searchRoute':
            ans = routes.searchRoute(**fc.args)
            print("Open src/output/output.json to see the result")
            outputAsJson("src/output/output", ans)
        elif fc.name == 'searchStop':
            print("Open src/output/output.json to see the result")
            outputAsJson("src/output/output", stops.searchStop(**fc.args))
        elif fc.name == 'searchPath':
            print("Open src/output/output.json to see the result")
            outputAsJson("src/output/output", paths.searchPath(**fc.args))
        part = chat.history[len(chat.history) - 1].parts[0]
        print(type(part).to_dict(part))


    
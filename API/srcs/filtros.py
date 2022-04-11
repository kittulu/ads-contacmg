def filtro():
    r_json = request.json
    param = r_json['param']
    data = r_json['data']
    query = "Select * from {param} where {data} like {param}.value"
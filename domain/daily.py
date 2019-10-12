daily = {
    'schema':{
        'date':{
            'type':'datetime',
            'required': True,
            'unique':True
        },
        'close':{'type':'number'},
        'pred_close':{'type':'number'},
    }
}
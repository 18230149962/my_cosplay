import string

model = 'GPTeamMemberInvestCaseModel'
model_key = 'GPTeamMemberInvestCase'
name = 'gp_team_member_invest_case'
service = 'gp_service'


model_str = '''
class {model}(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_deleted = db.Column(db.Boolean, default=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company_model.id'))
    dt_create = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    dt_update = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        ret_dict = dict()
        columns = [k.name for k in self.__table__.columns]
        for k in columns:
            value = getattr(self, k)
            if isinstance(value, datetime.datetime):
                value = int(utils.utcdatetime2ts(value))
            if isinstance(value, Decimal) and (value is not None) :
                if value == 0:
                    value = '0'
                value = str(value)
            if isinstance(value, bool):
                value = int(value)
            ret_dict[k] = value
        return ret_dict
'''.format(model=model)

view = '''
class Create{model_key}View(Api):
    decorators = [login_required]
    params_dict = dict()

    def logic_func(self, params):
        company_id = current_user.company_id
        current_user_id = current_user.id
        data = dict()
        for key in self.params_dict.keys():
            data[key] = params.get(key)
        data = {service}.create_{name}_process(company_id, data)
        return data


class Update{model_key}View(Api):
    decorators = [login_required]
    params_dict = dict()

    def logic_func(self, params):
        company_id = current_user.company_id
        current_user_id = current_user.id
        data = dict()
        for key in self.params_dict.keys():
            data[key] = params.get(key)
        data = {service}.update_{name}_process(company_id, data)
        return data


class Delete{model_key}View(Api):
    decorators = [login_required]
    params_dict = dict()

    def logic_func(self, params):
        company_id = current_user.company_id
        current_user_id = current_user.id
        obj_id = params.get('id')
        {service}.delete_{name}_process(company_id, obj_id)


class List{model_key}View(Api):
    decorators = [login_required]
    params_dict = dict()

    def logic_func(self, params):
        company_id = current_user.company_id
        current_user_id = current_user.id
        data = dict()
        data['company_id'] = company_id
        data['page_num'] = params.get('page_num')
        data['page_size'] = params.get('page_size')
        data = {service}.list_{name}_process(**data)
        return data


class {model_key}View(Api):
    decorators = [login_required]
    params_dict = dict()

    def logic_func(self, params):
        company_id = current_user.company_id
        current_user_id = current_user.id
        obj_id = params.get('id')
        data = {service}.get_{name}_process(company_id, obj_id)
        return data
'''.format(model=model, name=name, service=service, model_key=model_key)

backend = '''
@transaction.atomic(db)
def create_{name}_process(company_id, data_dict):
    data_dict['company_id'] = company_id
    obj = api_obj.create_obj(data_dict, {model})
    data = obj.to_dict()
    return data


@transaction.atomic(db)
def update_{name}_process(company_id, data_dict):
    if 'id' not in data_dict.keys():
        raise errors.InvalidArgsError('记录id不存在')
    obj_id = data_dict.get('id')
    obj = api_obj.is_existed_obj_by_id(company_id, obj_id, {model})
    if not obj:
        raise errors.InvalidArgsError('记录不存在或已被删除')
    data_dict['company_id'] = company_id
    data_dict.pop('id', None)
    obj = api_obj.update_obj_by_id(company_id, obj_id, data_dict, {model})
    data = obj.to_dict()
    return data


@transaction.atomic(db)
def delete_{name}_process(company_id, obj_id):
    obj = api_obj.is_existed_obj_by_id(company_id, obj_id, {model})
    if not obj:
        raise errors.InvalidArgsError('记录不存在或已被删除')
    api_obj.delete_obj_by_id(company_id, obj_id, {model})


def list_{name}_process(company_id, page_num=None, page_size=None):
    query = dict()
    query['company_id'] = company_id
    query['obj_model'] = {model}
    total = api_obj.obj_total(**query)
    query['page_num'] = page_num
    query['page_size'] = page_size
    objs = api_obj.list_objs(**query)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data_list.append(data)
    data = dict()
    data['total'] = total
    data['data_list'] = data_list
    return data


def get_{name}_process(company_id, obj_id):
    obj = api_obj.is_existed_obj_by_id(company_id, obj_id, {model})
    if not obj:
        raise errors.InvalidArgsError('录不存在或已被删除')
    data = obj.to_dict()
    return data
'''.format(name=name, model=model)

print(model_str, view, backend)

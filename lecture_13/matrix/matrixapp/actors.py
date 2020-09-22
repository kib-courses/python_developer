class Actor:
    msg_id = None
    fallback = 'not talking with strangers'

    def interact(self, *args, **kwargs):
        raise NotImplementedError


class WhiteRabbit(Actor):
    msg_id = 'white_rabbit'

    def disable(self):
        self.enabled = not self.enabled

    def __str__(self):
        return f'WhiteRabbit girl: (enabled={self.enabled})'

    def __init__(self):
        self.enabled = False
        self.name = 'White Rabbit'
        self.job = 'party girl'
        self.is_awaken = False
        self.people_to_search = None

    def interact(self, actor: Actor):
        if actor.msg_id == Neo.msg_id:
            return 'Definitely'
        else:
            return self.fallback


class Neo(Actor):
    msg_id = 'neo'

    def disable(self):
        self.enabled = not self.enabled

    def __str__(self):
        return f'Neo: (enabled={self.enabled})'

    def __init__(self):
        self.enabled = False
        self.name = 'Thomas Anderson'
        self.job = 'program writer'
        self.is_awaken = False
        self.people_to_search = ['Morpheus']

    def sleep(self):
        if not self.is_awaken:
            return 'Hardly'
        else:
            return 'Good'

    def fly(self):
        if self.job != 'program writer':
            return True
        else:
            return False

    def interact(self, actor: Actor):
        if actor.msg_id == WhiteRabbit.msg_id:
            return 'I have to work tomorrow'
        elif actor.msg_id == Morpheus.msg_id:
            return 'Thought it wasnt real'
        else:
            return self.fallback


class Morpheus(Actor):
    msg_id = 'morpheus'

    def __str__(self):
        return f'Morpheus: (enabled={self.enabled})'

    def disable(self):
        self.enabled = not self.enabled

    def __init__(self):
        self.enabled = False
        self.name = 'Morpheus'
        self.job = 'terrorist'
        self.is_awaken = True
        self.people_to_search = ['Neo']

    def interact(self, actor: Actor):
        if actor.msg_id == Neo.msg_id:
            return 'Your mind makes it real'
        else:
            return self.fallback



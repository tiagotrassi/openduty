from slacker import Slacker

class SlackNotifier:

    def __init__(self, config):
        self.__config = config
    
    def notify(self, notification):
        slack = Slacker(self.__config['xoxp-202075823266-202075823458-202078565794-22ee9b3e42b2621e76911e68ef44cb7b'])
        response = slack.chat.post_message(notification.user_to_notify.profile.slack_room_name, notification.message,
                                           username="Openduty", icon_url="https://slack.global.ssl.fastly.net/1937/img/services/pagerduty_48.png")
        if not response.error:
            print "Slack message sent"
        else:
            print "Failed to send Slack message"

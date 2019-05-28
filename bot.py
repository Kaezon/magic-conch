import logging
import os
import random
import sys

import discord

logger = logging.getLogger("MagicConch")
bot_token = os.getenv("BOT_TOKEN", "")

response_list = [
    "No.",
    "Maybe someday.",
    "I don't think so.",
    "Try Asking again.",
    "Yes."
]


class MagicConch(discord.Client):
    async def on_ready(self):
        logger.info(discord.utils.oauth_url(self.user.id))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if self.user.mentioned_in(message):
            await message.channel.send(random.choice(response_list))


if __name__ == "__main__":
    if not bot_secret:
        logger.error("BOT_SECRET needs to be set in the environment!")
        sys.exit(1)
    client = MagicConch()
    client.run(bot_token)

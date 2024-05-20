import neat
import yfinance as yf

from leather import Leather


def get_btc_data():
    BTC_Ticker =yf.download(tickers='BTC-USD', period = '3d', interval = '1m')
    return BTC_Ticker


def eval_genomes(genomes, config):

    all_data = get_btc_data()
    open_data = all_data['Open'].tolist()
    norm_open_data = [float(i) / max(open_data) for i in open_data]
    close_data = all_data['Close'].tolist()
    norm_close_data = [float(i) / max(close_data) for i in close_data]
    high_data = all_data['High'].tolist()
    norm_high_data = [float(i) / max(high_data) for i in high_data]
    low_data = all_data['Low'].tolist()
    norm_low_data = [float(i) / max(low_data) for i in low_data]
    volume_data = all_data['Volume'].tolist()
    norm_volume_data = [float(i) / max(volume_data) for i in volume_data]

    for genome_id, genome in genomes:
        # do stuff
        genome.fitness = 0

        wallet = Leather()
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        for day in range(len(open_data)):
            day_list = norm_open_data[day], norm_close_data[day], norm_high_data[day], norm_low_data[day], \
                norm_volume_data[day]

            action_decimal = net.activate(day_list)
            action = action_decimal.index(max(action_decimal)) + 1
            # print("Dec: {}, Action; {}".format(action_decimal, action))
            if action == 1:
                wallet.buy(close_data[day])
                # print("Buying, wallet now at: {}".format(wallet.usd_wallet))
            elif action == 2:
                wallet.sell(close_data[day])
                # print("Seling, wallet now at: {}".format(wallet.usd_wallet))

        wallet.sell(close_data[len(close_data)-1])
        genome.fitness = wallet.usd_wallet

        # loop through data
        # on each day tak inputs (date, price, volume, wallet)
        # take action (buy, sell, hold)
        # fitness equals to final wallet


def neat_run(config_path):
    # sets up config path, this is all preset stuff so ignore
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    # create population
    pop = neat.Population(config)

    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    # pop.add_reporter(neat.Checkpointer(1))

    best = pop.run(eval_genomes, 100)


if __name__ == '__main__':
    # lets see
    config = "/Users/anatolii/PycharmProjects/pythonTesting/tradingBot/neat_test.config"

    neat_run(config)


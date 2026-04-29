import pygame
import random
import sys

# --- CONFIGURAZIONE ---
SCREEN_WIDTH, SCREEN_HEIGHT = 1100, 750
FPS = 60

# Palette Cromatica
GOLD, DARK_GOLD = (212, 175, 55), (150, 120, 40)
DEEP_BLUE, TABLE_BORDER = (20, 30, 60), (10, 15, 35)
CARD_WHITE, CARD_BACK = (250, 250, 250), (40, 100, 200)
RED_SUIT, BLACK_SUIT = (200, 20, 20), (30, 30, 30)

# Colori Fiches
CHIP_COLORS = {
    10: (50, 150, 50),   # Verde
    50: (50, 100, 200),  # Blu
    100: (30, 30, 30),   # Nero
    500: (180, 0, 0)     # Rosso scuro
}

RISK_FACTS = [
    "Il 'Near Miss' (quasi vincita) inganna il cervello facendogli credere di essere vicino a vincere.",
    "La velocità del gioco digitale impedisce al lobo frontale di valutare razionalmente le perdite.",
    "Il banco vince sempre nel lungo periodo grazie alla trattenuta matematica (RTP).",
    "La dipendenza da gioco d'azzardo altera i circuiti della dopamina come le droghe pesanti.",
    "Inseguire le perdite è la via più veloce verso il tracollo finanziario."
]

class Card:
    def __init__(self, suit, rank):
        self.suit, self.rank = suit, rank
        self.value = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}[rank]
        self.pos = [SCREEN_WIDTH // 2, -200]
        self.target = [0, 0]
        self.speed = 20
        self.held = False

    def update_pos(self):
        dx, dy = self.target[0] - self.pos[0], self.target[1] - self.pos[1]
        dist = (dx**2 + dy**2)**0.5
        if dist > self.speed:
            self.pos[0] += dx/dist * self.speed
            self.pos[1] += dy/dist * self.speed
        else: self.pos = list(self.target)

class PokerGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Video Poker Responsabile")
        self.clock = pygame.time.Clock()
        
        self.font_title = pygame.font.SysFont("Garamond", 50, bold=True)
        self.font_card = pygame.font.SysFont("Arial", 28, bold=True)
        self.font_ui = pygame.font.SysFont("Verdana", 18, bold=True)
        self.font_warn = pygame.font.SysFont("Verdana", 15, italic=True)

        self.balance = 1000
        self.bet = 0
        self.state = "BETTING" # BETTING, DRAWING (scelta carte), RESULT, BANKRUPT
        self.hand = []
        self.msg = "PIAZZA LA TUA SCOMMESSA"
        self.current_warn = random.choice(RISK_FACTS)
        self.warn_timer = 0
        self.reset_deck()

    def reset_deck(self):
        suits, ranks = ['♥', '♦', '♣', '♠'], ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.deck = [Card(s, r) for s in suits for r in ranks]
        random.shuffle(self.deck)

    def deal_hand(self):
        self.hand = []
        for i in range(5):
            card = self.deck.pop()
            card.target = [180 + i*150, 300]
            self.hand.append(card)

    def draw_new_cards(self):
        for i in range(5):
            if not self.hand[i].held:
                card = self.deck.pop()
                card.pos = [180 + i*150, -150]
                card.target = [180 + i*150, 300]
                self.hand[i] = card
        self.evaluate_result()

    def evaluate_result(self):
        values = sorted([c.value for c in self.hand])
        suits = [c.suit for c in self.hand]
        counts = {v: values.count(v) for v in set(values)}
        occ = sorted(counts.values(), reverse=True)
        is_flush = len(set(suits)) == 1
        is_straight = all(values[i] == values[0] + i for i in range(5))

        mult = 0
        if is_flush and is_straight and values[0] == 10: self.msg = "SCALA REALE!"; mult = 250
        elif is_flush and is_straight: self.msg = "SCALA COLORE"; mult = 50
        elif occ[0] == 4: self.msg = "POKER!"; mult = 25
        elif occ[0] == 3 and occ[1] == 2: self.msg = "FULL HOUSE"; mult = 9
        elif is_flush: self.msg = "COLORE"; mult = 6
        elif is_straight: self.msg = "SCALA"; mult = 4
        elif occ[0] == 3: self.msg = "TRIS"; mult = 3
        elif occ[0] == 2 and occ[1] == 2: self.msg = "DOPPIA COPPIA"; mult = 2
        elif occ[0] == 2 and any(v >= 11 for v, c in counts.items() if c == 2): self.msg = "COPPIA VESTITA"; mult = 1
        else: self.msg = "NESSUNA COMBINAZIONE"; mult = 0

        self.balance += (self.bet * mult)
        self.bet = 0
        self.state = "RESULT"
        if self.balance <= 0: self.state = "BANKRUPT"

    def draw_chip(self, val, x, y):
        m, click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        rect = pygame.Rect(x-35, y-35, 70, 70)
        hover = rect.collidepoint(m)
        
        pygame.draw.circle(self.screen, (20,20,20), (x+3, y+3), 35) # Ombra
        pygame.draw.circle(self.screen, CHIP_COLORS[val], (x, y), 35 if not hover else 38)
        pygame.draw.circle(self.screen, (255,255,255), (x, y), 30, 2)
        txt = self.font_ui.render(str(val), True, (255,255,255))
        self.screen.blit(txt, (x - txt.get_width()//2, y - txt.get_height()//2))

        if hover and click[0] and self.state == "BETTING":
            if self.balance >= val:
                self.balance -= val
                self.bet += val
                pygame.time.delay(150)

    def run(self):
        while True:
            self.screen.fill(TABLE_BORDER)
            pygame.draw.rect(self.screen, DEEP_BLUE, (50, 50, 1000, 600), border_radius=50)
            pygame.draw.rect(self.screen, GOLD, (50, 50, 1000, 600), 3, border_radius=50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.state == "DRAWING":
                    for card in self.hand:
                        if pygame.Rect(card.pos[0], card.pos[1], 110, 160).collidepoint(event.pos):
                            card.held = not card.held

            # Update Warning
            if self.balance < 500 or self.state == "BANKRUPT":
                self.warn_timer += 1
                if self.warn_timer % 180 == 0: self.current_warn = random.choice(RISK_FACTS)

            # Disegno Carte
            for c in self.hand:
                c.update_pos()
                self.draw_card_ui(c)

            # UI Basso
            pygame.draw.rect(self.screen, BLACK_SUIT, (0, 650, 1100, 100))
            self.screen.blit(self.font_ui.render(f"CREDITI: €{self.balance}", True, GOLD), (50, 675))
            self.screen.blit(self.font_ui.render(f"PUNTATA: €{self.bet}", True, (200,200,200)), (50, 705))
            
            if self.balance < 500 and self.state != "BANKRUPT":
                w_surf = self.font_warn.render(f"ATTENZIONE: {self.current_warn}", True, GOLD)
                self.screen.blit(w_surf, (SCREEN_WIDTH//2 - w_surf.get_width()//2, 620))

            # Messaggio Stato
            m_surf = self.font_title.render(self.msg, True, GOLD)
            self.screen.blit(m_surf, (SCREEN_WIDTH//2 - m_surf.get_width()//2, 120))

            # Logica Pulsanti e Fiches
            if self.state == "BETTING":
                self.draw_chip(10, 950, 120)
                self.draw_chip(50, 950, 210)
                self.draw_chip(100, 950, 300)
                self.draw_chip(500, 950, 390)
                if self.btn("GIOCA", 450, 675, 200, 45, (20, 80, 20)) and self.bet > 0:
                    self.reset_deck()
                    self.deal_hand()
                    self.state = "DRAWING"
                    self.msg = "CLICCA LE CARTE DA TENERE"
                if self.btn("RESET", 700, 675, 120, 45, (60, 60, 60)):
                    self.balance += self.bet; self.bet = 0

            elif self.state == "DRAWING":
                if self.btn("CAMBIA CARTE", 450, 675, 200, 45, (150, 20, 20)):
                    self.draw_new_cards()

            elif self.state == "RESULT":
                if self.btn("PROSSIMA MANO", 450, 675, 200, 45, (40, 40, 40)):
                    self.state = "BETTING"
                    self.msg = "PIAZZA LA TUA SCOMMESSA"
                    self.hand = []

            elif self.state == "BANKRUPT":
                self.draw_bankrupt_overlay()

            pygame.display.flip()
            self.clock.tick(FPS)

    def draw_card_ui(self, card):
        x, y = card.pos
        rect = pygame.Rect(x, y, 110, 160)
        pygame.draw.rect(self.screen, (0,0,0,50), rect.move(5,5), border_radius=12)
        pygame.draw.rect(self.screen, CARD_WHITE, rect, border_radius=12)
        pygame.draw.rect(self.screen, GOLD if not card.held else (200, 50, 50), rect, 3 if not card.held else 5, border_radius=12)
        
        color = RED_SUIT if card.suit in ['♥', '♦'] else BLACK_SUIT
        self.screen.blit(self.font_card.render(card.rank, True, color), (x+10, y+10))
        self.screen.blit(self.font_card.render(card.suit, True, color), (x+10, y+45))
        if card.held:
            h_txt = self.font_ui.render("TENUTA", True, (200, 50, 50))
            self.screen.blit(h_txt, (x + (110-h_txt.get_width())//2, y+130))

    def btn(self, text, x, y, w, h, color):
        m, click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        rect = pygame.Rect(x, y, w, h)
        hover = rect.collidepoint(m)
        pygame.draw.rect(self.screen, ([min(c+40,255) for c in color] if hover else color), rect, border_radius=8)
        t = self.font_ui.render(text, True, (255,255,255))
        self.screen.blit(t, (x+(w-t.get_width())//2, y+(h-t.get_height())//2))
        if hover and click[0]: pygame.time.delay(200); return True
        return False

    def draw_bankrupt_overlay(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 245))
        self.screen.blit(overlay, (0,0))
        t = self.font_title.render("SOLDI FINITI", True, (200, 50, 50))
        self.screen.blit(t, (SCREEN_WIDTH//2 - t.get_width()//2, 200))
        f = pygame.font.SysFont("Georgia", 22, italic=True).render(self.current_warn, True, (230, 230, 230))
        self.screen.blit(f, (SCREEN_WIDTH//2 - f.get_width()//2, 350))
        h = self.font_ui.render("SERVIZIO AIUTO: 800 55 88 22", True, GOLD)
        self.screen.blit(h, (SCREEN_WIDTH//2 - h.get_width()//2, 450))
        e = self.font_warn.render("Premi ESC per chiudere", True, (100, 100, 100))
        self.screen.blit(e, (SCREEN_WIDTH//2 - e.get_width()//2, 600))
        if pygame.key.get_pressed()[pygame.K_ESCAPE]: pygame.quit(); sys.exit()

if __name__ == "__main__":
    PokerGame().run()
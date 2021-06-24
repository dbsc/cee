import { signin, signIn, signOut, useSession } from 'next-auth/client'
import styles from './styles.module.scss'

export function Hero() {
	const [session] = useSession()

	const botao = session ? (
		<button onClick={() => signOut()}>{session.user.name}</button>
	) : (
		<button onClick={() => signIn('google')}>Fazer Login</button>
	)

	return (
		<div className={styles.container}>
			<div className={styles.content}>
				<img src="/logos/logo_white.svg" alt="CEE" />
				<p>
					A <span>CEE</span> é uma liga universitária que trabalha para conectar os alunos do ITA às
					melhores oportunidades do mercado de trabalho
				</p>
				<div className={styles.buttons}>
					{botao}
					<button type="button" onClick={(e) => {e.preventDefault(); 
						window.location.href='https://forms.gle/V3oNNjSKr5ZnQtQT8'}}>
						Divulgar vaga no ITA</button>
				</div>
			</div>
		</div>
	)
}

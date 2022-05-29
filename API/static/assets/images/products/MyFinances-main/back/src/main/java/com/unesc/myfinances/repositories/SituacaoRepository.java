package com.unesc.myfinances.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.unesc.myfinances.entities.Situacao;

@Repository
public interface SituacaoRepository extends JpaRepository<Situacao, Long>{

}
